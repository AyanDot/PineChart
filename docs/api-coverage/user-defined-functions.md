---
layout: default
title: User-Defined Functions
parent: API Coverage
nav_order: 30
---

## User-Defined Functions

| Feature                    | Status | Description                              |
|----------------------------|--------|------------------------------------------|
| Single-line `f(x) => expr` | ✅    | Arrow function                           |
| Multi-line block body      | ✅     | Indented block                           |
| Default parameters         | ✅     | `f(src, int len = 14)`                   |
| Named arguments            | ✅     | `f(length = 20, src = close)`            |
| Nested function calls      | ✅     | User functions calling user functions    |
| `var`/`varip` in functions | ✅     | Persistent state inside functions        |
| Recursion guard            | ✅     | Max depth 50                             |
| `method` keyword           | ✅     | Parsed as function def with isMethod     |
| `export` keyword           | ✅     | Skipped (no library support)             |
