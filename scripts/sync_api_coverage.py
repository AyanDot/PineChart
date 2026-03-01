#!/usr/bin/env python3
"""Generate PineChart API coverage docs from the canonical tracker.

Usage:
    python "PineChart Web/scripts/sync_api_coverage.py"
    python "PineChart Web/scripts/sync_api_coverage.py" --check
    python "PineChart Web/scripts/sync_api_coverage.py" --source "<path>" --docs-dir "<path>"
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence


@dataclass(frozen=True)
class SectionSpec:
    number: int
    source_name: str
    slug: str
    title: str
    nav_order: int


@dataclass(frozen=True)
class ParsedSection:
    number: int
    name: str
    body: str


SECTION_SPECS: Sequence[SectionSpec] = (
    SectionSpec(1, "Array", "array", "Array", 1),
    SectionSpec(2, "Builtin", "builtin", "Builtin", 2),
    SectionSpec(3, "Barstate", "barstate", "Barstate", 3),
    SectionSpec(4, "Box", "box", "Box", 4),
    SectionSpec(5, "Chart", "chart", "Chart", 5),
    SectionSpec(6, "Color", "color", "Color", 6),
    SectionSpec(7, "Control Flow", "control-flow", "Control Flow", 7),
    SectionSpec(8, "Input", "input", "Input", 8),
    SectionSpec(9, "Label", "label", "Label", 9),
    SectionSpec(10, "Line", "line", "Line", 10),
    SectionSpec(11, "Linefill", "linefill", "Linefill", 11),
    SectionSpec(12, "Log", "log", "Log", 12),
    SectionSpec(13, "Map", "map", "Map", 13),
    SectionSpec(14, "Math", "math", "Math", 14),
    SectionSpec(15, "Matrix", "matrix", "Matrix", 15),
    SectionSpec(16, "Others", "others", "Others", 16),
    SectionSpec(17, "Plots", "plots", "Plots", 17),
    SectionSpec(18, "Polyline", "polyline", "Polyline", 18),
    SectionSpec(19, "Request", "request", "Request", 19),
    SectionSpec(20, "Runtime", "runtime", "Runtime", 20),
    SectionSpec(21, "Session", "session", "Session", 21),
    SectionSpec(22, "String", "str", "String", 22),
    SectionSpec(23, "Table", "table", "Table", 23),
    SectionSpec(24, "Technical Analysis", "ta", "Technical Analysis", 24),
    SectionSpec(25, "Timeframe", "timeframe", "Timeframe", 25),
    SectionSpec(26, "Types", "types", "Types", 26),
    SectionSpec(27, "Strategy", "strategy", "Strategy", 27),
    SectionSpec(28, "Syminfo", "syminfo", "Syminfo", 28),
    SectionSpec(29, "User-Defined Types", "user-defined-types", "User-Defined Types", 29),
    SectionSpec(30, "User-Defined Functions", "user-defined-functions", "User-Defined Functions", 30),
    SectionSpec(31, "Operators", "operators", "Operators", 31),
)

LINK_GROUPS: Sequence[tuple[str, Sequence[str]]] = (
    (
        "Core Namespaces",
        (
            "builtin",
            "input",
            "math",
            "ta",
            "array",
            "str",
            "request",
            "timeframe",
            "barstate",
            "runtime",
            "session",
            "syminfo",
            "types",
        ),
    ),
    (
        "Charting & Drawing",
        (
            "chart",
            "color",
            "plots",
            "box",
            "label",
            "line",
            "linefill",
            "polyline",
            "table",
        ),
    ),
    ("Data Structures & Utilities", ("log", "map", "matrix", "others")),
    (
        "Language & Strategy",
        ("control-flow", "operators", "user-defined-functions", "user-defined-types", "strategy"),
    ),
)

SECTION_HEADER_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)


def parse_metrics(source_text: str) -> Dict[str, str]:
    patterns = {
        "total": r"(?im)^Total Functions:\s*(\d+)\s*$",
        "percentage": r"(?im)^Percentage Implemented:\s*([^\n]+?)\s*$",
        "implemented": r"(?im)^\s*-\s*✅\s*Fully Implemented:\s*(\d+)\s*$",
        "partial": r"(?im)^\s*-\s*🟡\s*Partially Implemented:\s*(\d+)\s*$",
        "not_implemented": r"(?im)^\s*-\s*🔴\s*Not Implemented:\s*(\d+)\s*$",
        "planned": r"(?im)^\s*-\s*🔵\s*Planned Next:\s*(\d+)\s*$",
        "low_priority": r"(?im)^\s*-\s*⚪\s*Low Priority:\s*(\d+)\s*$",
    }
    values: Dict[str, str] = {}
    missing: List[str] = []
    for key, pattern in patterns.items():
        match = re.search(pattern, source_text)
        if not match:
            missing.append(key)
            continue
        values[key] = match.group(1).strip()

    if missing:
        raise ValueError(f"Missing required tracker metrics: {', '.join(missing)}")
    return values


def _strip_trailing_divider(body: str) -> str:
    lines = body.splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and lines[-1].strip() == "---":
        lines.pop()
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def _is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def _is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not _is_table_line(stripped):
        return False
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if not cells:
        return False
    for cell in cells:
        if not re.fullmatch(r":?-{3,}:?", cell):
            return False
    return True


def _is_table_start(lines: Sequence[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    return _is_table_line(lines[index]) and _is_table_separator(lines[index + 1])


def _normalize_table_spacing(body: str) -> str:
    lines = body.splitlines()
    if not lines:
        return body

    out: List[str] = []
    for index, line in enumerate(lines):
        if _is_table_start(lines, index):
            if out and out[-1].strip():
                out.append("")

        out.append(line.rstrip())

        next_line = lines[index + 1] if index + 1 < len(lines) else ""
        if _is_table_line(line) and next_line and not _is_table_line(next_line):
            if next_line.strip() and (not out or out[-1].strip()):
                out.append("")

    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


def parse_sections(source_text: str) -> Dict[int, ParsedSection]:
    matches = list(SECTION_HEADER_RE.finditer(source_text))
    if not matches:
        raise ValueError("No numbered API sections found in source tracker.")

    sections: Dict[int, ParsedSection] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        name = match.group(2).strip()
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(source_text)
        body = source_text[body_start:body_end].strip("\n")
        body = _strip_trailing_divider(body)
        body = _normalize_table_spacing(body)
        if body:
            body = body.rstrip() + "\n"
        sections[number] = ParsedSection(number=number, name=name, body=body)
    return sections


def validate_sections(parsed_sections: Dict[int, ParsedSection]) -> None:
    expected_by_number = {spec.number: spec for spec in SECTION_SPECS}
    parsed_numbers = set(parsed_sections)
    expected_numbers = set(expected_by_number)

    missing = sorted(expected_numbers - parsed_numbers)
    extra = sorted(parsed_numbers - expected_numbers)
    if missing:
        raise ValueError(f"Missing expected numbered sections in tracker: {missing}")
    if extra:
        raise ValueError(f"Found unmapped numbered sections in tracker: {extra}")

    mismatches: List[str] = []
    for number, spec in expected_by_number.items():
        parsed = parsed_sections[number]
        if parsed.name != spec.source_name:
            mismatches.append(
                f"Section {number}: expected '{spec.source_name}', found '{parsed.name}'"
            )
    if mismatches:
        raise ValueError("Section heading mismatches:\n" + "\n".join(mismatches))


def render_child(spec: SectionSpec, parsed: ParsedSection) -> str:
    lines = [
        "---",
        "layout: default",
        f"title: {spec.title}",
        "parent: API Coverage",
        f"nav_order: {spec.nav_order}",
        "---",
        "",
        f"## {spec.title}",
        "",
    ]
    body = parsed.body
    if body:
        lines.append(body.rstrip("\n"))
        lines.append("")
    return "\n".join(lines)


def render_parent(metrics: Dict[str, str], specs: Sequence[SectionSpec]) -> str:
    specs_by_slug = {spec.slug: spec for spec in specs}
    for _, slugs in LINK_GROUPS:
        for slug in slugs:
            if slug not in specs_by_slug:
                raise ValueError(f"Parent link group references unknown slug '{slug}'")

    lines: List[str] = [
        "---",
        "layout: default",
        "title: API Coverage",
        "nav_order: 4",
        "permalink: /api-coverage/",
        "has_children: true",
        "---",
        "",
        "# Pine Script API Coverage",
        "",
        (
            f"PineChart implements **{metrics['implemented']} out of {metrics['total']}** "
            f"Pine Script v5/v6 API functions ({metrics['percentage']})."
        ),
        "",
        "## Legend",
        "",
        f"- ✅ Fully Implemented ({metrics['implemented']})",
        f"- 🟡 Partially Implemented ({metrics['partial']})",
        f"- 🔴 Not Implemented ({metrics['not_implemented']})",
        f"- 🔵 Planned Next ({metrics['planned']})",
        f"- ⚪ Low Priority ({metrics['low_priority']})",
        "",
    ]

    for group_title, slugs in LINK_GROUPS:
        lines.append(f"## {group_title}")
        lines.append("")
        for slug in slugs:
            spec = specs_by_slug[slug]
            lines.append(f"- [{spec.title}](./api-coverage/{spec.slug}.md)")
        lines.append("")
    return "\n".join(lines)


def build_outputs(source_text: str, docs_dir: Path) -> Dict[Path, str]:
    metrics = parse_metrics(source_text)
    parsed_sections = parse_sections(source_text)
    validate_sections(parsed_sections)

    outputs: Dict[Path, str] = {}
    outputs[docs_dir / "api-coverage.md"] = render_parent(metrics, SECTION_SPECS)
    child_dir = docs_dir / "api-coverage"
    for spec in SECTION_SPECS:
        parsed = parsed_sections[spec.number]
        outputs[child_dir / f"{spec.slug}.md"] = render_child(spec, parsed)
    return outputs


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def run_check(outputs: Dict[Path, str], docs_dir: Path) -> int:
    mismatches: List[str] = []

    for path, expected in sorted(outputs.items()):
        if not path.exists():
            mismatches.append(f"Missing file: {path}")
            continue
        current = read_file(path)
        if current != expected:
            mismatches.append(f"Out of sync: {path}")

    child_dir = docs_dir / "api-coverage"
    expected_children = {path for path in outputs if path.parent == child_dir}
    existing_children = set(child_dir.glob("*.md")) if child_dir.exists() else set()
    unexpected = sorted(existing_children - expected_children)
    for path in unexpected:
        mismatches.append(f"Unexpected child page: {path}")

    if mismatches:
        print("API coverage docs are not in sync:")
        for mismatch in mismatches:
            print(f"  - {mismatch}")
        return 1

    print("API coverage docs are in sync.")
    return 0


def run_write(outputs: Dict[Path, str]) -> int:
    changed_paths: List[Path] = []
    for path, expected in sorted(outputs.items()):
        current = read_file(path) if path.exists() else None
        if current == expected:
            continue
        write_file(path, expected)
        changed_paths.append(path)

    if changed_paths:
        print(f"Wrote {len(changed_paths)} API coverage doc file(s):")
        for path in changed_paths:
            print(f"  - {path}")
    else:
        print("No changes. API coverage docs are already up to date.")
    return 0


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    default_source = script_dir.parent.parent / "Pine API Tracker.md"
    default_docs_dir = script_dir.parent / "docs"

    parser = argparse.ArgumentParser(
        description="Sync PineChart API coverage docs from Pine API Tracker.md."
    )
    parser.add_argument("--check", action="store_true", help="Validate generated docs without writing.")
    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help=f"Path to source tracker markdown. Default: {default_source}",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=default_docs_dir,
        help=f"Path to PineChart docs directory. Default: {default_docs_dir}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = args.source.resolve()
    docs_dir = args.docs_dir.resolve()

    if not source_path.exists():
        print(f"Source tracker not found: {source_path}", file=sys.stderr)
        return 1
    if not source_path.is_file():
        print(f"Source path is not a file: {source_path}", file=sys.stderr)
        return 1
    if not docs_dir.exists():
        print(f"Docs directory not found: {docs_dir}", file=sys.stderr)
        return 1
    if not docs_dir.is_dir():
        print(f"Docs path is not a directory: {docs_dir}", file=sys.stderr)
        return 1

    source_text = read_file(source_path)
    outputs = build_outputs(source_text, docs_dir)

    if args.check:
        return run_check(outputs, docs_dir)
    return run_write(outputs)


if __name__ == "__main__":
    sys.exit(main())
