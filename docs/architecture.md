---
layout: default
title: Architecture
nav_order: 3
---

# Architecture

An overview of how PineChart executes Pine Script inside MetaTrader 5.

---

## Pipeline Overview

PineChart processes Pine Script through a classic interpreter pipeline:

```
Pine Script (.txt file)
    │
    ▼
┌─────────┐     ┌─────────┐     ┌──────────────┐
│  Lexer  │ ──▶ │ Parser  │ ──▶ │ Interpreter  │
│ (tokens)│     │  (AST)  │     │ (per-bar exec)│
└─────────┘     └─────────┘     └──────────────┘
                                       │
                                       ▼
                              Plots / Drawings / Orders
```

1. **Lexer** — Tokenizes Pine Script source into 70+ token types, with indentation tracking for Python-style blocks
2. **Parser** — Recursive descent parser builds an AST with 18+ node types (if/else, for/while, switch, function definitions, UDTs, etc.)
3. **Interpreter** — Executes the AST per-bar with full Pine Script semantics: series reverse-access, `var`/`varip` persistence, NA propagation

---

## Per-Bar Execution Model

Pine Script runs once per bar, from bar 0 (oldest) to the current bar. This is fundamentally different from event-driven MQL5 programming.

- Each bar, the interpreter walks the entire AST
- Built-in variables (`open`, `high`, `low`, `close`, `volume`) reflect the current bar's data
- Series access with `[N]` looks back N bars from the current position
- `var` variables initialize once and persist across all bars
- `varip` variables persist across bars AND intrabar ticks

**Calculate-once, render-visible**: Pine executes once over full history (up to `InpMaxBars`, default 5000). Plot arrays store all computed values. Panning and scrolling only changes the visible offset — no recalculation needed.

### Indicators vs Strategies: Tick Recalculation

**Indicators** execute per-bar only. Once a bar is calculated, its values are final. When a new tick arrives, the indicator does not re-execute — it waits for the next confirmed bar.

**Strategies** execute per-tick on the latest bar. Because strategies submit real orders, they need to react to intrabar price changes. PineChart handles this with a snapshot-restore cycle:

1. Before the last bar, all TA states are snapshotted
2. On each new tick, states are restored to the snapshot and the last bar is re-executed with updated OHLCV data
3. This gives strategies fresh signal evaluation on every tick without recalculating the entire 5000-bar history

This means `barstate.isrealtime` and `barstate.isconfirmed` behave differently in strategies — a strategy sees multiple executions per bar (one per tick), while an indicator sees exactly one.

---

## Technical Analysis Engine

TA functions compute incrementally using persistent state:

- Each TA call gets a unique state slot via a monotonic counter (`ta.sma@0`, `ta.sma@1`, etc.)
- State includes circular buffers (`values[]`), running sums, and recursive formula accumulators
- Composite functions (like `ta.bb` which uses `ta.sma` + `ta.stdev`) chain sub-functions with unique sub-keys
- Tuple-return functions return array handles that get destructured automatically

The TA engine spans 6 category modules:
- **Moving Averages** — SMA, EMA, RMA, WMA, VWMA, HMA, SWMA
- **Oscillators** — RSI, MACD, Momentum, ROC, Change, CMO
- **Volatility** — True Range, ATR, StDev, Variance
- **Statistics** — Highest, Lowest, Cumulative Sum, Linear Regression
- **Signals** — Crossover, Crossunder, Cross, Rising, Falling
- **Indicators** — Stochastic, CCI, Williams %R, Bollinger Bands, SuperTrend, DMI, Parabolic SAR, Pivot Points

---

## Multi-Indicator Architecture

PineChart can run N indicators + 1 optional strategy simultaneously:

- Each indicator gets its own isolated execution context (variable scope, UDT pool, table pool, cached AST)
- All indicators share bar data, the plot manager, drawing store, and multi-timeframe data pool
- Plot index offsets prevent cross-indicator collisions
- Indicators are specified via comma-separated filenames in the `InpIndicators` input

---

## Rendering Model

Everything draws on an **optimized canvas** — chart, UI, plots, crosshair, drawings, tables. The rendering pipeline is designed for smooth, lag-free performance with zero flicker, even with multiple indicators and drawing objects active.

**Smart indicator panes**: Each indicator can render in the main chart pane (overlay) or in its own sub-pane below, with independent price scales and auto-scaling. Pane dividers are draggable.

**Theme system**: EA color inputs feed a `ThemeManager` that auto-derives a complete readable palette consumed by all renderers and UI components.

---

## Strategy Execution

Pine Script `strategy.*` functions map directly to MQL5's CTrade library:

- `strategy.entry()` / `strategy.order()` → `CTrade::Buy()` / `CTrade::Sell()`
- `strategy.close()` / `strategy.close_all()` → `CTrade::PositionClose()`
- `strategy.exit()` → `CTrade::PositionModify()` (SL/TP)
- `strategy.cancel()` / `strategy.cancel_all()` → `CTrade::OrderDelete()`

No custom backtester — MT5's Strategy Tester provides backtesting for free. Live bar gating ensures real trades only execute on the latest bar.

---

## NA Propagation

PineChart faithfully implements Pine Script's NA (Not Available) semantics:

- `na` propagates correctly throughout the system
- TA functions return `na` during their warmup period (first N-1 bars)
- Arithmetic with `na` propagates: `na + 5 = na`
- Plot gaps are rendered correctly when values are `na`
- Auto-scaling excludes `na` values

This ensures that composable TA expressions like `ta.linreg(ta.sma(close, 20) - ta.highest(high, 20), 20, 0)` produce correct results — inner NAs during warmup propagate cleanly through the chain.
