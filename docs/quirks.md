---
layout: default
title: Known Quirks
nav_order: 5
---

# Known Quirks & Limitations

Important behaviors and limitations to be aware of when using PineChart.

---

## `request.security()` — Market Watch Only

`request.security()` can only fetch data for symbols that are **already in your Market Watch** window. If you request a symbol that isn't visible in Market Watch, the data will not load.

**Workaround**: Before running your script, add all required symbols to Market Watch (right-click Market Watch > Show All, or search and add individual symbols).

---

## `input.*` Returns Defaults Only

All `input.*` functions (14 types) are implemented but currently return their `defval` (default value) only. There is no UI integration yet — you cannot change input values from a settings panel.

**Workaround**: Edit the default values directly in your Pine Script source file.

---

## Series Lookback on TA Results Not Supported

Applying the history-reference operator `[]` to the result of a TA function call is not yet supported:

```
// This does NOT work yet:
prevSma = ta.sma(close, 20)[1]

// Workaround: store in a variable first
currentSma = ta.sma(close, 20)
prevSma = currentSma[1]
```

---

## `for item in array` Support

The `for item in collection` loop syntax is supported for arrays. You can use either `for item in array` or index-based loops depending on your script style.

---

## NA Propagation Behavior

PineChart faithfully implements Pine Script's `na` (Not Available) semantics. Be aware:

- TA functions return `na` for the first N-1 bars (warmup period)
- Any arithmetic with `na` produces `na`
- Comparison with `na` returns `false` (e.g., `na > 5` is false)
- Use `nz()` to replace `na` with a fallback value
- Use `na()` function to test for `na` (not `== na`)

---

## Drawing Object Limits

Each drawing type (line, label, box) has a **500-object limit** with FIFO (first-in, first-out) eviction. If your script creates more than 500 objects of one type, the oldest objects are automatically deleted.

This matches TradingView's behavior where similar limits apply.

---

## Unsupported Functions Return `na` or `0`

When your script calls a function that PineChart hasn't implemented yet, the interpreter:

1. Logs a message in the MT5 **Experts** tab identifying the function
2. Returns `na` or `0` depending on context
3. Continues executing the rest of your script

Your script won't crash — it will just have missing data for unsupported calls.

---

## Instance Method Syntax Not Supported

Pine Script allows calling array methods on the object directly (e.g., `myArr.push(5)`). PineChart currently only supports the namespace form:

```
// This does NOT work yet:
myArr.push(5)

// Use this instead:
array.push(myArr, 5)
```

---

## Multi-Timeframe Limitations

`request.security()` currently supports:

- Simple OHLCV field access (`close`, `open`, `high`, `low`, `volume`)
- Cross-symbol data (any symbol in Market Watch)
- Higher-timeframe alignment with `gaps` and `lookahead` control
- Tuple returns

**Not yet supported**:
- TA expressions inside `request.security()` (e.g., `request.security(sym, tf, ta.sma(close, 20))`)
- `request.security_lower_tf()` for lower timeframe data

---

## Strategy Specifics

- **Strategies recalculate per-tick; indicators do not.** On the latest bar, strategies re-execute on every incoming tick so they can react to intrabar price changes and submit orders in real time. Indicators only execute once per confirmed bar. This means `barstate.isrealtime` fires multiple times per bar in a strategy but effectively once in an indicator.
- Strategies use MQL5's CTrade for order execution — filling modes and order types depend on your broker
- `strategy.exit()` trailing stop is not yet supported
- `strategy.closedtrades.*` and `strategy.opentrades.*` history functions (14 functions) are planned but not yet implemented
- Backtesting uses MT5's built-in Strategy Tester (no custom backtester)

---

## MQL5 Platform Constraints

These are inherent to the MQL5 environment, not PineChart-specific:

- **No regex support**: `str.match()` performs simple substring matching, not full regex
- **WebRequest restrictions**: `request.security()` for cross-symbol data requires the symbol to be in Market Watch because MQL5 uses broker-provided data, not web APIs
- **Timer resolution**: The chart refreshes on a 16ms timer cycle, which is sufficient for most use cases but differs from TradingView's web-based rendering

---

## Not Yet Implemented (Major Categories)

For the full function-by-function status, see the [API Coverage](api-coverage) page. Major missing categories include:

- **Map** — `map.*` (11 functions)
- **Matrix** — `matrix.*` (40+ functions)
- **Linefill** — `linefill.*` (7 functions)
- **Polyline** — `polyline.*` (3 functions)
- **Log** — `log.*` (3 functions)
- **Date/Time functions** — `dayofmonth()`, `hour()`, `timestamp()`, etc.
- **Plot variants** — `plotarrow()`, `plotbar()`, `plotcandle()`
