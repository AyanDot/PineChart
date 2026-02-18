---
layout: default
title: API Coverage
nav_order: 4
---

# Pine Script API Coverage

PineChart implements **294 out of 701** Pine Script v5/v6 API functions (~42%).

**Legend:**
- ✅ Implemented (294)
- 🔵 Planned (219)
- 🔴 Not Yet Implemented (175)
- 🟡 Partial (2)

---

## 1. Array

### Creation & Initialization

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.copy()` | ✅ | Create copy of array |
| `array.from()` | ✅ | Create array from arguments |
| `array.new_bool()` | ✅ | Create boolean array |
| `array.new_box()` | 🔵 | Create box array |
| `array.new_color()` | 🔵 | Create color array |
| `array.new_float()` | ✅ | Create float array |
| `array.new_int()` | ✅ | Create int array |
| `array.new_label()` | 🔵 | Create label array |
| `array.new_line()` | 🔵 | Create line array |
| `array.new_linefill()` | 🔵 | Create linefill array |
| `array.new_string()` | 🔵 | Create string array |
| `array.new_table()` | 🔵 | Create table array |
| `array.new<type>()` | 🔵 | Create typed array (generic) |

### Element Access

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.first()` | ✅ | Get first element |
| `array.get()` | ✅ | Get value at index |
| `array.last()` | ✅ | Get last element |
| `array.set()` | ✅ | Set value at index |

### Modification

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.clear()` | ✅ | Remove all elements |
| `array.fill()` | ✅ | Fill array with value |
| `array.insert()` | ✅ | Insert element at index |
| `array.pop()` | ✅ | Remove last element |
| `array.push()` | ✅ | Append element to end |
| `array.remove()` | ✅ | Remove element at index |
| `array.reverse()` | ✅ | Reverse order |
| `array.shift()` | ✅ | Remove first element |
| `array.unshift()` | ✅ | Prepend element |

### Size & Shape

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.concat()` | ✅ | Concatenate arrays |
| `array.size()` | ✅ | Get array size |
| `array.slice()` | ✅ | Extract subarray |

### Search & Query

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.binary_search()` | 🔵 | Binary search |
| `array.binary_search_leftmost()` | 🔵 | Binary search (leftmost) |
| `array.binary_search_rightmost()` | 🔵 | Binary search (rightmost) |
| `array.includes()` | ✅ | Check if value exists |
| `array.indexof()` | ✅ | Find first index of value |
| `array.lastindexof()` | ✅ | Find last index of value |

### Statistical

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.avg()` | ✅ | Average of elements |
| `array.covariance()` | ✅ | Covariance |
| `array.max()` | ✅ | Maximum value |
| `array.median()` | ✅ | Median value |
| `array.min()` | ✅ | Minimum value |
| `array.mode()` | ✅ | Mode value |
| `array.range()` | ✅ | Range of values |
| `array.stdev()` | ✅ | Standard deviation |
| `array.sum()` | ✅ | Sum of elements |
| `array.variance()` | ✅ | Variance |

### Percentiles

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.percentile_linear_interpolation()` | 🔵 | Percentile (Linear) |
| `array.percentile_nearest_rank()` | 🔵 | Percentile (Nearest Rank) |
| `array.percentrank()` | 🔵 | Percentile rank |

### Transformation

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.abs()` | ✅ | Absolute values |
| `array.join()` | 🔵 | Join to string |
| `array.sort()` | ✅ | Sort array |
| `array.sort_indices()` | 🔵 | Get sorted indices |
| `array.standardize()` | 🔵 | Standardize elements |

### Logical

| Function | Status | Description |
|:---------|:-------|:------------|
| `array.every()` | ✅ | Check if all elements match |
| `array.some()` | ✅ | Check if any element matches |

---

## 2. Built-in Variables & Functions

### Variables

| Function | Status | Description |
|:---------|:-------|:------------|
| `bar_index` | ✅ | Current bar index |
| `close` | ✅ | Close price |
| `high` | ✅ | High price |
| `hl2` | ✅ | Average of high and low |
| `hlc3` | ✅ | Average of high, low, and close |
| `hlcc4` | 🔵 | Average of high, low, close, close |
| `last_bar_index` | 🔵 | Index of last bar |
| `last_bar_time` | 🔵 | Time of last bar |
| `low` | ✅ | Low price |
| `na` | ✅ | Not a number literal |
| `ohlc4` | ✅ | Average of OHLC |
| `open` | ✅ | Open price |
| `timenow` | 🔵 | Current time |
| `volume` | ✅ | Volume |
| `ask` | 🔵 | Ask price |
| `bid` | 🔵 | Bid price |
| `time` | 🔵 | Bar time |
| `time_close` | 🔵 | Bar close time |

### Constants

| Function | Status |
|:---------|:-------|
| `true` | ✅ |
| `false` | ✅ |

### Functions

| Function | Status | Description |
|:---------|:-------|:------------|
| `indicator()` | ✅ | Indicator declaration |
| `input()` | ✅ | Input parameter (returns defval) |
| `na()` | 🔵 | Check if value is NaN |
| `nz()` | ✅ | Replace NaN with zero |
| `strategy()` | ✅ | Strategy declaration |
| `hline()` | ✅ | Horizontal line |
| `box()` | ✅ | Box object |
| `label()` | ✅ | Label object |
| `line()` | ✅ | Line object |

---

## 3. Barstate

| Function | Status | Description |
|:---------|:-------|:------------|
| `barstate.isconfirmed` | ✅ | Bar is confirmed |
| `barstate.isfirst` | ✅ | First bar of dataset |
| `barstate.ishistory` | ✅ | Bar is historical |
| `barstate.islast` | ✅ | Last bar of dataset |
| `barstate.islastconfirmedhistory` | ✅ | Last confirmed historical bar |
| `barstate.isnew` | ✅ | New bar |
| `barstate.isrealtime` | ✅ | Bar is real-time |

---

## 4. Box

### Management

| Function | Status | Description |
|:---------|:-------|:------------|
| `box.new()` | ✅ | Create new box |
| `box.delete()` | ✅ | Delete box |
| `box.all` | 🔵 | All boxes collection |
| `box.copy()` | 🔵 | Copy box |

### Getters

| Function | Status | Description |
|:---------|:-------|:------------|
| `box.get_bottom()` | ✅ | Get bottom coordinate |
| `box.get_left()` | ✅ | Get left coordinate |
| `box.get_right()` | ✅ | Get right coordinate |
| `box.get_top()` | ✅ | Get top coordinate |

### Setters

| Function | Status | Description |
|:---------|:-------|:------------|
| `box.set_bgcolor()` | ✅ | Set background color |
| `box.set_border_color()` | ✅ | Set border color |
| `box.set_border_style()` | 🔵 | Set border style |
| `box.set_border_width()` | ✅ | Set border width |
| `box.set_bottom()` | ✅ | Set bottom coordinate |
| `box.set_left()` | ✅ | Set left coordinate |
| `box.set_lefttop()` | ✅ | Set left-top point |
| `box.set_right()` | ✅ | Set right coordinate |
| `box.set_rightbottom()` | ✅ | Set right-bottom point |
| `box.set_top()` | ✅ | Set top coordinate |
| `box.set_text()` | 🔵 | Set text |
| `box.set_text_color()` | 🔵 | Set text color |
| `box.set_extend()` | 🔵 | Set extend mode |

---

## 5. Color

### Predefined Colors

| Color | Status |
|:------|:-------|
| `color.black` | ✅ |
| `color.blue` | ✅ |
| `color.gray` | ✅ |
| `color.green` | ✅ |
| `color.lime` | ✅ |
| `color.red` | ✅ |
| `color.white` | ✅ |
| `color.aqua` | ✅ |
| `color.navy` | ✅ |
| `color.orange` | ✅ |
| `color.purple` | ✅ |
| `color.yellow` | ✅ |
| `color.maroon` | 🔵 |
| `color.fuchsia` | 🔵 |
| `color.olive` | 🔵 |
| `color.silver` | 🔵 |
| `color.teal` | 🔵 |

### Color Functions

| Function | Status | Description |
|:---------|:-------|:------------|
| `color.new()` | 🔵 | Create new color |
| `color.rgb()` | 🔵 | Create from RGB |
| `color.r()` | 🔵 | Get red component |
| `color.g()` | 🔵 | Get green component |
| `color.b()` | 🔵 | Get blue component |
| `color.t()` | 🔵 | Get transparency |
| `color.from_gradient()` | 🔵 | Create from gradient |

---

## 6. Control Flow

### Conditionals

| Feature | Status |
|:--------|:-------|
| `if` statement | ✅ |
| `if...else` | ✅ |
| `if...else if` chain | ✅ |
| Nested `if`/`else` | ✅ |
| `if` as expression | ✅ |
| `switch` statement | ✅ |
| `switch` as expression | ✅ |
| Ternary `? :` | ✅ |

### Loops

| Feature | Status | Notes |
|:--------|:-------|:------|
| `for i = start to end` | ✅ | |
| `for i = start to end by step` | ✅ | |
| `for item in collection` | 🟡 | Parsed, runtime not ready |
| `while` loop | ✅ | |
| `break` | ✅ | |
| `continue` | ✅ | |

### Variable Declaration

| Feature | Status |
|:--------|:-------|
| `var` | ✅ |
| `varip` | ✅ |

---

## 7. Input

All input types are implemented and return their default value (`defval`). No UI integration yet.

| Function | Status |
|:---------|:-------|
| `input()` | ✅ |
| `input.bool()` | ✅ |
| `input.color()` | ✅ |
| `input.enum()` | ✅ |
| `input.float()` | ✅ |
| `input.int()` | ✅ |
| `input.price()` | ✅ |
| `input.session()` | ✅ |
| `input.source()` | ✅ |
| `input.string()` | ✅ |
| `input.symbol()` | ✅ |
| `input.text_area()` | ✅ |
| `input.time()` | ✅ |
| `input.timeframe()` | ✅ |

---

## 8. Label

### Management

| Function | Status |
|:---------|:-------|
| `label.new()` | ✅ |
| `label.delete()` | ✅ |
| `label.all` | 🔵 |
| `label.copy()` | 🔵 |

### Getters

| Function | Status |
|:---------|:-------|
| `label.get_text()` | ✅ |
| `label.get_x()` | ✅ |
| `label.get_y()` | ✅ |

### Setters

| Function | Status |
|:---------|:-------|
| `label.set_color()` | ✅ |
| `label.set_size()` | ✅ |
| `label.set_style()` | ✅ |
| `label.set_text()` | ✅ |
| `label.set_textcolor()` | ✅ |
| `label.set_x()` | ✅ |
| `label.set_xy()` | ✅ |
| `label.set_y()` | ✅ |
| `label.set_point()` | 🔵 |
| `label.set_textalign()` | 🔵 |
| `label.set_tooltip()` | 🔵 |
| `label.set_xloc()` | 🔵 |
| `label.set_yloc()` | 🔵 |

### Styles

| Style | Status |
|:------|:-------|
| `label.style_arrowdown` | ✅ |
| `label.style_arrowup` | ✅ |
| `label.style_circle` | ✅ |
| `label.style_cross` | ✅ |
| `label.style_diamond` | ✅ |
| `label.style_label_center` | ✅ |
| `label.style_label_down` | ✅ |
| `label.style_label_left` | ✅ |
| `label.style_label_right` | ✅ |
| `label.style_label_up` | ✅ |
| `label.style_none` | ✅ |
| `label.style_square` | ✅ |
| `label.style_triangledown` | ✅ |
| `label.style_triangleup` | ✅ |

---

## 9. Line

### Management

| Function | Status |
|:---------|:-------|
| `line.new()` | ✅ |
| `line.delete()` | ✅ |
| `line.all` | 🔵 |
| `line.copy()` | 🔵 |

### Getters

| Function | Status |
|:---------|:-------|
| `line.get_x1()` | ✅ |
| `line.get_x2()` | ✅ |
| `line.get_y1()` | ✅ |
| `line.get_y2()` | ✅ |
| `line.get_price()` | 🔵 |

### Setters

| Function | Status |
|:---------|:-------|
| `line.set_color()` | ✅ |
| `line.set_extend()` | ✅ |
| `line.set_style()` | ✅ |
| `line.set_width()` | ✅ |
| `line.set_x1()` | ✅ |
| `line.set_x2()` | ✅ |
| `line.set_xy1()` | ✅ |
| `line.set_xy2()` | ✅ |
| `line.set_y1()` | ✅ |
| `line.set_y2()` | ✅ |
| `line.set_xloc()` | 🔵 |

### Styles

| Style | Status |
|:------|:-------|
| `line.style_arrow_both` | ✅ |
| `line.style_arrow_left` | ✅ |
| `line.style_arrow_right` | ✅ |
| `line.style_dashed` | ✅ |
| `line.style_dotted` | ✅ |
| `line.style_solid` | ✅ |

---

## 10. Linefill

All linefill functions are **not yet implemented** (🔴).

`linefill.new()`, `linefill.delete()`, `linefill.set_color()`, `linefill.get_line1()`, `linefill.get_line2()`, `linefill.all`

---

## 11. Log

All log functions are **not yet implemented** (🔴).

`log.error()`, `log.info()`, `log.warning()`

---

## 12. Map

All map functions are **not yet implemented** (🔴).

`map.new<type,type>()`, `map.get()`, `map.put()`, `map.contains()`, `map.keys()`, `map.values()`, `map.size()`, `map.clear()`, `map.copy()`, `map.put_all()`, `map.remove()`

---

## 13. Math

### Constants

| Constant | Status |
|:---------|:-------|
| `math.e` | 🔵 |
| `math.phi` | 🔵 |
| `math.pi` | 🔵 |
| `math.rphi` | 🔵 |

### Basic Operations

| Function | Status |
|:---------|:-------|
| `math.abs()` | ✅ |
| `math.ceil()` | ✅ |
| `math.floor()` | ✅ |
| `math.round()` | ✅ |
| `math.sign()` | ✅ |
| `math.round_to_mintick()` | 🔵 |

### Exponential & Logarithmic

| Function | Status |
|:---------|:-------|
| `math.exp()` | ✅ |
| `math.log()` | ✅ |
| `math.log10()` | ✅ |
| `math.pow()` | ✅ |
| `math.sqrt()` | ✅ |

### Statistical

| Function | Status |
|:---------|:-------|
| `math.max()` | ✅ |
| `math.min()` | ✅ |
| `math.avg()` | 🔵 |
| `math.sum()` | 🔵 |

### Trigonometric

| Function | Status |
|:---------|:-------|
| `math.cos()` | 🔵 |
| `math.sin()` | 🔵 |
| `math.tan()` | 🔵 |
| `math.acos()` | 🔵 |
| `math.asin()` | 🔵 |
| `math.atan()` | 🔵 |

---

## 14. Matrix

All matrix functions (40+) are **not yet implemented** (🔴). This includes creation, element access, modification, statistical, operations, linear algebra, properties, and sorting.

---

## 15. Plots

| Function | Status | Description |
|:---------|:-------|:------------|
| `plot()` | ✅ | Plot a series |
| `hline()` | ✅ | Horizontal line |
| `plotchar()` | 🔴 | Plot character markers |
| `plotshape()` | 🔴 | Plot shape markers |
| `plotarrow()` | 🔴 | Plot arrow markers |
| `plotbar()` | 🔴 | Plot bar chart |
| `plotcandle()` | 🔴 | Plot candlestick chart |
| `barcolor()` | 🔴 | Set bar color |
| `bgcolor()` | 🔴 | Set background color |

---

## 16. Request

| Function | Status | Description |
|:---------|:-------|:------------|
| `request.security()` | ✅ | Multi-timeframe/cross-symbol data (simple OHLCV fields) |
| `request.security_lower_tf()` | 🔵 | Lower timeframe data |
| `request.currency_rate()` | 🔴 | Currency rate |
| `request.splits()` | 🔴 | Splits data |

---

## 17. String

### Query

| Function | Status |
|:---------|:-------|
| `str.contains()` | ✅ |
| `str.endswith()` | ✅ |
| `str.length()` | ✅ |
| `str.match()` | 🟡 (substring only, no regex) |
| `str.pos()` | ✅ |
| `str.startswith()` | ✅ |

### Formatting

| Function | Status |
|:---------|:-------|
| `str.format()` | ✅ |
| `str.format_time()` | ✅ |

### Transformation

| Function | Status |
|:---------|:-------|
| `str.lower()` | ✅ |
| `str.repeat()` | ✅ |
| `str.replace()` | ✅ |
| `str.replace_all()` | ✅ |
| `str.trim()` | ✅ |
| `str.upper()` | ✅ |

### Parsing & Conversion

| Function | Status |
|:---------|:-------|
| `str.split()` | 🔵 |
| `str.substring()` | ✅ |
| `str.tonumber()` | ✅ |
| `str.tostring()` | ✅ |

---

## 18. Strategy

### Declaration

| Function | Status |
|:---------|:-------|
| `strategy()` | ✅ |

### Order Functions

| Function | Status | Description |
|:---------|:-------|:------------|
| `strategy.entry()` | ✅ | Submit entry order |
| `strategy.close()` | ✅ | Close by entry ID |
| `strategy.close_all()` | ✅ | Close all positions |
| `strategy.exit()` | ✅ | Set SL/TP exit |
| `strategy.order()` | ✅ | Submit generic order |
| `strategy.cancel()` | ✅ | Cancel pending order |
| `strategy.cancel_all()` | ✅ | Cancel all pending |

### Properties

| Property | Status |
|:---------|:-------|
| `strategy.position_size` | ✅ |
| `strategy.position_avg_price` | ✅ |
| `strategy.equity` | ✅ |
| `strategy.openprofit` | ✅ |
| `strategy.netprofit` | ✅ |
| `strategy.initial_capital` | ✅ |
| `strategy.closedtrades` | ✅ |
| `strategy.opentrades` | ✅ |
| `strategy.wintrades` | ✅ |
| `strategy.losstrades` | ✅ |
| `strategy.grossprofit` | 🔵 |
| `strategy.grossloss` | 🔵 |
| `strategy.max_drawdown` | 🔵 |

### Constants

| Constant | Status |
|:---------|:-------|
| `strategy.long` | ✅ |
| `strategy.short` | ✅ |

### Trade History Functions

All `strategy.closedtrades.*` and `strategy.opentrades.*` functions (15 total) are **planned** (🔵).

---

## 19. Table

### Cell Operations

| Function | Status |
|:---------|:-------|
| `table.cell()` | ✅ |
| `table.cell_set_bgcolor()` | ✅ |
| `table.cell_set_height()` | ✅ |
| `table.cell_set_text()` | ✅ |
| `table.cell_set_text_color()` | ✅ |
| `table.cell_set_text_halign()` | ✅ |
| `table.cell_set_text_size()` | ✅ |
| `table.cell_set_text_valign()` | ✅ |
| `table.cell_set_tooltip()` | ✅ |
| `table.cell_set_width()` | ✅ |
| `table.merge_cells()` | 🔵 |

### Management

| Function | Status |
|:---------|:-------|
| `table.new()` | ✅ |
| `table.clear()` | ✅ |
| `table.delete()` | ✅ |

### Settings

| Function | Status |
|:---------|:-------|
| `table.set_bgcolor()` | ✅ |
| `table.set_border_color()` | ✅ |
| `table.set_border_width()` | ✅ |
| `table.set_frame_color()` | ✅ |
| `table.set_frame_width()` | ✅ |
| `table.set_position()` | ✅ |

---

## 20. Technical Analysis

### Moving Averages

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.ema()` | ✅ | Exponential Moving Average |
| `ta.hma()` | ✅ | Hull Moving Average |
| `ta.linreg()` | ✅ | Linear Regression |
| `ta.rma()` | ✅ | Rolling Moving Average |
| `ta.sma()` | ✅ | Simple Moving Average |
| `ta.swma()` | ✅ | Symmetrically Weighted MA |
| `ta.vwma()` | ✅ | Volume Weighted MA |
| `ta.wma()` | ✅ | Weighted Moving Average |
| `ta.alma()` | 🔵 | Arnaud Legoux MA |
| `ta.vwap()` | 🔵 | Volume Weighted Average Price |

### Oscillators & Momentum

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.cci()` | ✅ | Commodity Channel Index |
| `ta.change()` | ✅ | Price Change |
| `ta.cmo()` | ✅ | Chande Momentum Oscillator |
| `ta.macd()` | ✅ | MACD |
| `ta.mom()` | ✅ | Momentum |
| `ta.roc()` | ✅ | Rate of Change |
| `ta.rsi()` | ✅ | Relative Strength Index |
| `ta.stoch()` | ✅ | Stochastic |
| `ta.wpr()` | ✅ | Williams %R |
| `ta.cog()` | 🔵 | Center of Gravity |
| `ta.mfi()` | 🔵 | Money Flow Index |
| `ta.tsi()` | 🔵 | True Strength Index |

### Volatility & Range

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.tr` | ✅ | True Range (variable) |
| `ta.atr()` | ✅ | Average True Range |
| `ta.bb()` | ✅ | Bollinger Bands |
| `ta.stdev()` | ✅ | Standard Deviation |
| `ta.variance()` | ✅ | Variance |
| `ta.bbw()` | 🔵 | Bollinger Bands Width |
| `ta.kc()` | 🔵 | Keltner Channels |
| `ta.dev()` | 🔵 | Mean Absolute Deviation |

### Trend Analysis

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.cross()` | ✅ | Cross (either direction) |
| `ta.crossover()` | ✅ | Crossover |
| `ta.crossunder()` | ✅ | Crossunder |
| `ta.dmi()` | ✅ | Directional Movement Index |
| `ta.falling()` | ✅ | Falling Detection |
| `ta.rising()` | ✅ | Rising Detection |
| `ta.sar()` | ✅ | Parabolic SAR |
| `ta.supertrend()` | ✅ | SuperTrend |

### Statistical

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.correlation()` | ✅ | Correlation Coefficient |
| `ta.highest()` | ✅ | Highest Value |
| `ta.lowest()` | ✅ | Lowest Value |
| `ta.highestbars()` | 🔵 | Bars Since Highest |
| `ta.lowestbars()` | 🔵 | Bars Since Lowest |

### Utility

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.barssince()` | ✅ | Bars Since Condition |
| `ta.cum()` | ✅ | Cumulative Sum |
| `ta.valuewhen()` | ✅ | Value When Condition Met |

### Support & Resistance

| Function | Status | Description |
|:---------|:-------|:------------|
| `ta.pivothigh()` | ✅ | Pivot High |
| `ta.pivotlow()` | ✅ | Pivot Low |
| `ta.pivot_point_levels()` | 🔵 | Pivot Point Levels |

---

## 21. Timeframe

| Property | Status |
|:---------|:-------|
| `timeframe.isdaily` | ✅ |
| `timeframe.isdwm` | ✅ |
| `timeframe.isintraday` | ✅ |
| `timeframe.ismonthly` | ✅ |
| `timeframe.isweekly` | ✅ |
| `timeframe.multiplier` | ✅ |
| `timeframe.period` | ✅ |
| `timeframe.isminutes` | 🔴 |
| `timeframe.isseconds` | 🔴 |
| `timeframe.isticks` | 🔴 |

---

## 22. Syminfo

| Property | Status |
|:---------|:-------|
| `syminfo.tickerid` | ✅ |
| `syminfo.ticker` | ✅ |
| `syminfo.mintick` | ✅ |
| `syminfo.pointvalue` | ✅ |
| `syminfo.currency` | ✅ |
| `syminfo.basecurrency` | ✅ |
| `syminfo.description` | 🔵 |
| `syminfo.type` | 🔵 |
| `syminfo.timezone` | 🔵 |

---

## 23. User-Defined Types

| Feature | Status |
|:--------|:-------|
| `type` declaration | ✅ |
| `TypeName.new()` | ✅ |
| Field access `obj.field` | ✅ |
| Field assignment `:=` | ✅ |
| `var` persistence | ✅ |
| `na` handling | ✅ |
| `obj.copy()` | ✅ |
| Method calls | ✅ |
| `array<UDT>` fields | 🔵 |

---

## 24. User-Defined Functions

| Feature | Status |
|:--------|:-------|
| Single-line `f(x) => expr` | ✅ |
| Multi-line block body | ✅ |
| Default parameters | ✅ |
| Named arguments | ✅ |
| Nested function calls | ✅ |
| `var`/`varip` in functions | ✅ |
| Recursion guard (max 50) | ✅ |
| `method` keyword | ✅ |
| `export` keyword | ✅ (skipped, no library support) |

---

## 25. Operators

| Operator | Status |
|:---------|:-------|
| `+` `-` `*` `/` `%` | ✅ |
| `==` `!=` `>` `<` `>=` `<=` | ✅ |
| `and` `or` `not` | ✅ |
| `=` `:=` `+=` `-=` `*=` `/=` | ✅ |
| `[]` (series access) | ✅ |

---

## 26. Constants & Types

### Barmerge

| Constant | Status |
|:---------|:-------|
| `barmerge.gaps_off` | ✅ |
| `barmerge.gaps_on` | ✅ |
| `barmerge.lookahead_off` | ✅ |
| `barmerge.lookahead_on` | ✅ |

### Extend

| Constant | Status |
|:---------|:-------|
| `extend.both` | ✅ |
| `extend.left` | ✅ |
| `extend.none` | ✅ |
| `extend.right` | ✅ |

### Position

| Constant | Status |
|:---------|:-------|
| `position.bottom_center` | ✅ |
| `position.bottom_left` | ✅ |
| `position.bottom_right` | ✅ |
| `position.middle_center` | ✅ |
| `position.middle_left` | ✅ |
| `position.middle_right` | ✅ |
| `position.top_center` | ✅ |
| `position.top_left` | ✅ |
| `position.top_right` | ✅ |

### Size

| Constant | Status |
|:---------|:-------|
| `size.auto` | ✅ |
| `size.huge` | ✅ |
| `size.large` | ✅ |
| `size.normal` | ✅ |
| `size.small` | ✅ |
| `size.tiny` | ✅ |

### Hline Styles

| Constant | Status |
|:---------|:-------|
| `hline.style_dashed` | ✅ |
| `hline.style_dotted` | ✅ |
| `hline.style_solid` | ✅ |

### Text Alignment

| Constant | Status |
|:---------|:-------|
| `text.align_center` | ✅ |
| `text.align_left` | ✅ |
| `text.align_right` | ✅ |

---

## Categories Not Yet Started

The following categories are entirely **not yet implemented** (🔴):

- **Chart** — `chart.*` (properties, type detection, visible range, chart points)
- **Session** — `session.*` (flags, constants)
- **Polyline** — `polyline.*`
- **Log** — `log.*`
- **Map** — `map.*`
- **Matrix** — `matrix.*`
- **Runtime** — `runtime.error()`
- **Date/Time functions** — `dayofmonth()`, `hour()`, `timestamp()`, etc.
- **Display constants** — `display.*`
- **Format constants** — `format.*`
- **Location constants** — `location.*`
- **Scale constants** — `scale.*`
- **Shape constants** — `shape.*`
