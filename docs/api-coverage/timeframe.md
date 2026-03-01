---
layout: default
title: Timeframe
parent: API Coverage
nav_order: 25
---

## Timeframe

### Timeframe Type Checks
| Function             | Status | Description                   |
|----------------------|--------|-------------------------------|
| timeframe.isdaily    | ✅     | Check if daily timeframe      |
| timeframe.isdwm      | ✅     | Check if daily/weekly/monthly |
| timeframe.isintraday | ✅     | Check if intraday timeframe   |
| timeframe.isminutes  | ✅     | Check if minutes timeframe    |
| timeframe.ismonthly  | ✅     | Check if monthly timeframe    |
| timeframe.isseconds  | ✅     | Check if seconds timeframe (always false in MT5) |
| timeframe.isticks    | ✅     | Check if ticks timeframe (always false in MT5)   |
| timeframe.isweekly   | ✅     | Check if weekly timeframe     |

### Timeframe Properties
| Function              | Status | Description              |
|-----------------------|--------|--------------------------|
| timeframe.main_period | 🔴     | Main period of timeframe |
| timeframe.multiplier  | ✅     | Timeframe multiplier     |
| timeframe.period      | ✅     | Timeframe period         |

### Timeframe Functions
| Function                 | Status | Description                   |
|--------------------------|--------|-------------------------------|
| timeframe.change()       | ✅     | Detect timeframe change (stub)|
| timeframe.from_seconds() | 🔴     | Create timeframe from seconds |
| timeframe.in_seconds()   | ✅     | Convert timeframe to seconds  |
