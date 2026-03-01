# PineChart — Run Pine Script in MetaTrader 5

**PineChart** is an MQL5 Expert Advisor that lets you run Pine Script indicators and strategies directly inside MetaTrader 5 — no manual conversion to MQL5 required.

**[Get PineChart on MQL5 Marketplace](https://www.mql5.com/en/market/product/164682)** | **[Download Free Demo](https://ayandot.github.io/PineChart/demo.html)** | **[Documentation](https://ayandot.github.io/PineChart/docs/)**

---

## Key Features

- **Full Pine Script Interpreter** — Built-in lexer, parser, and per-bar execution engine for Pine Script v5/v6
- **609+ Functions Implemented** — 79% of the Pine Script API and growing (69 TA functions, 47 array functions, 17 string functions, all 14 input types, strategy orders, math, color, date/time, and more)
- **Modern TradingView-Style Charts** — Full-canvas rendering with candlesticks, OHLC, line, area, Heiken Ashi, crosshair, zoom, and pan
- **Strategy Trading** — Pine Script strategies execute real orders through MQL5's CTrade library
- **Drawing Objects & Tables** — Lines, labels, boxes, hlines with handle-based pools; screen-anchored tables with 9 positions
- **Multi-Indicator & Multi-Timeframe** — Run multiple Pine Script indicators simultaneously; use `request.security()` for cross-timeframe data
- **User-Defined Types & Functions** — Full UDT support with constructors, field access, methods, and chained access
- **Interactive Trade Panel** — Market, Limit, Stop, Stop Limit, and Manage tabs with risk/reward and on-chart TP/SL drag
- **Alerts & Screener** — Runtime alert engine with Telegram & MetaQuotes notifications, mini-chart screener, bar replay mode

## How It Works

1. **Copy** your Pine Script indicator or strategy source code into a `.txt` file
2. **Paste** the file into MetaTrader 5's `MQL5/Files/` directory
3. **Enter** the filename in PineChart's EA input — done. Your script runs live in MT5.

## API Coverage

| Category | Coverage |
|----------|----------|
| Array | 85% |
| Technical Analysis | 100% |
| String | 94% |
| Input | 100% |
| Strategy | 54% |
| Drawing / Tables | 87% |
| Control Flow | 100% |
| Barstate / Syminfo | 100% |
| Math | 100% |
| Color | 100% |
| Date / Time | 86% |

**609 / 768** total Pine Script v5/v6 functions implemented (~79%).

## License

All rights reserved. PineChart is a commercial product available on the [MQL5 Marketplace](https://www.mql5.com/en/market/product/164682).
