---
layout: default
title: Getting Started
nav_order: 2
---

# Getting Started

Get PineChart running in three steps.

---

## Prerequisites

- **MetaTrader 5** installed (any broker)
- **PineChart EA** purchased from the [MQL5 Marketplace](https://www.mql5.com/en/market) (or use the free demo)

---

## Step 1: Copy Your Pine Script

Find the Pine Script indicator or strategy you want to use on TradingView. Copy the full source code into a `.txt` file.

PineChart supports Pine Script v5/v6 syntax including:
- `if`/`else`, `for`/`while`, `switch`, `var`/`varip`
- User-defined functions and types
- 294+ built-in functions

```
// Example: my_indicator.txt
//@version=5
indicator("My RSI", overlay=false)
length = input.int(14, "RSI Length")
src = input.source(close, "Source")
rsiValue = ta.rsi(src, length)
plot(rsiValue, "RSI", color=color.blue)
hline(70, "Overbought")
hline(30, "Oversold")
```

---

## Step 2: Place It in the MT5 Files Directory

Save your `.txt` file into MetaTrader 5's **MQL5/Files/** folder.

To find this folder:
1. Open MetaTrader 5
2. Go to **File > Open Data Folder**
3. Navigate to `MQL5/Files/`
4. Paste your `.txt` file here

You can add as many Pine Script files as you like. Each indicator runs in its own isolated execution context.

---

## Step 3: Attach PineChart and Enter the Filename

1. Drag PineChart onto any chart (or double-click it in the Navigator panel)
2. In the **Inputs** tab, find the `InpIndicators` field
3. Type the filename (e.g., `my_indicator.txt`)
4. For multiple indicators, use comma-separated filenames: `rsi.txt,macd.txt,bollinger.txt`
5. For a strategy, use the `InpStrategy` input field instead
6. Click **OK**

PineChart's lexer tokenizes, parser builds the AST, and the interpreter executes every bar — your Pine Script indicator is now running live in MetaTrader 5.

---

## Configuration Options

| Input | Description | Default |
|:------|:------------|:--------|
| `InpIndicators` | Comma-separated Pine Script indicator filenames | `PineScript.txt` |
| `InpStrategy` | Optional Pine Script strategy filename | (empty) |
| `InpMaxBars` | Maximum bars to calculate | 5000 |
| `InpChartGradient` | Chart background gradient toggle | true |
| `InpChartColor1` | Primary chart color | (dark theme) |
| `InpChartColor2` | Secondary chart color | (dark theme) |

---

## What to Expect

- **Indicators** render as plot lines on the canvas chart with the style defined in your Pine Script
- **Drawing objects** (line, label, box, hline) appear on the chart with FIFO eviction at 500 per type
- **Tables** appear at their configured screen position (e.g., `position.top_right`)
- **Strategies** execute real orders via MQL5's CTrade when running on a live/demo account, or backtest via MT5's Strategy Tester
- **Unsupported functions** log a message in the Experts tab and return `na` or `0` — the rest of your script continues to execute

---

## Next Steps

- Check the [API Coverage](api-coverage) page to see which functions your script uses
- Review [Known Quirks](quirks) for important limitations
- Read the [Architecture](architecture) overview to understand how the engine works
