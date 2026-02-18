---
layout: default
title: Home
nav_order: 1
permalink: /docs/
has_children: false
---

# PineChart Documentation

PineChart is an MQL5 Expert Advisor that runs Pine Script indicators and strategies directly inside MetaTrader 5. No manual conversion to MQL5 required.

{: .note }
PineChart currently implements **294 out of 701** Pine Script v5/v6 API functions (~42%), with coverage growing in every update.

---

## Quick Links

| Section | Description |
|:--------|:------------|
| [Getting Started](getting-started) | Install PineChart and run your first Pine Script indicator in MT5 |
| [Architecture](architecture) | How the Pine Script engine works under the hood |
| [API Coverage](api-coverage) | Full function-by-function implementation status |
| [Known Quirks](quirks) | Limitations and behaviors to be aware of |

---

## What PineChart Does

- **Runs Pine Script natively in MT5** — paste your `.txt` source file, type the filename, done
- **Full interpreter pipeline** — lexer, parser, and per-bar execution engine built entirely in MQL5
- **Modern charting UI** — TradingView-style candlesticks, crosshair, gradient themes, multi-pane layout
- **Strategy execution** — Pine Script `strategy.*` functions map to MQL5's CTrade for live and backtest trading
- **Multi-indicator support** — run N indicators simultaneously with isolated execution state
- **Multi-timeframe data** — `request.security()` for cross-symbol and higher-timeframe access

---

## Supported Pine Script Features

- All control flow: `if`/`else`, `for`, `while`, `switch`, ternary `? :`
- Variable persistence: `var`, `varip`
- User-defined functions with default/named arguments
- User-defined types (UDTs) with fields, methods, and chained access
- 37+ technical analysis functions (SMA, EMA, RSI, MACD, Bollinger Bands, SuperTrend, and more)
- 30+ array functions, 16 string functions, 14 input types
- Drawing objects: `line`, `label`, `box`, `hline` with handle-based pool
- Tables with 9 screen positions and auto-sized cells
- Plot styles: line, histogram, columns, circles, cross with per-bar dynamic colors
