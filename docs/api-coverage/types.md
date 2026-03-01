---
layout: default
title: Types
parent: API Coverage
nav_order: 26
---

## Types

### Dayofweek

| Function            | Status | Description |
|---------------------|--------|-------------|
| dayofweek.friday    | ✅     | Friday (6)  |
| dayofweek.monday    | ✅     | Monday (2)  |
| dayofweek.saturday  | ✅     | Saturday (7)|
| dayofweek.sunday    | ✅     | Sunday (1)  |
| dayofweek.thursday  | ✅     | Thursday (5)|
| dayofweek.tuesday   | ✅     | Tuesday (3) |
| dayofweek.wednesday | ✅     | Wednesday (4)|

### Barmerge

| Function               | Status | Description                          |
|------------------------|--------|--------------------------------------|
| barmerge.gaps_off      | ✅     | Fill gaps with last value (default)  |
| barmerge.gaps_on       | ✅     | Return na for non-HTF bars           |
| barmerge.lookahead_off | ✅     | Use previous completed bar (default) |
| barmerge.lookahead_on  | ✅     | Use current (incomplete) bar         |

### Display

| Function              | Status | Description              |
|-----------------------|--------|--------------------------|
| display.all           | ✅     | Display all              |
| display.data_window   | ✅     | Display in data window   |
| display.none          | ✅     | Display none             |
| display.pane          | ✅     | Display in pane          |
| display.pine_screener | 🔴     | Display in Pine Screener |
| display.price_scale   | ✅     | Display in price scale   |
| display.status_line   | ✅     | Display in status line   |

### Extend

| Function     | Status | Description  |
|--------------|--------|--------------|
| extend.both  | ✅     | Extend both  |
| extend.left  | ✅     | Extend left  |
| extend.none  | ✅     | Extend none  |
| extend.right | ✅     | Extend right |

### Font

| Function              | Status | Description           |
|-----------------------|--------|-----------------------|
| font.family_default   | ✅     | Default font family   |
| font.family_monospace | ✅     | Monospace font family |

### Format

| Function       | Status | Description    |
|----------------|--------|----------------|
| format.inherit | ✅     | Inherit format |
| format.mintick | ✅     | Mintick format |
| format.percent | ✅     | Percent format |
| format.price   | ✅     | Price format   |
| format.volume  | ✅     | Volume format  |

### Hline

| Function           | Status | Description                  |
|--------------------|--------|------------------------------|
| hline.style_dashed | ✅     | Dashed horizontal line style |
| hline.style_dotted | ✅     | Dotted horizontal line style |
| hline.style_solid  | ✅     | Solid horizontal line style  |

### Location

| Function          | Status | Description        |
|-------------------|--------|--------------------|
| location.abovebar | ✅     | Above bar location |
| location.absolute | ✅     | Absolute location  |
| location.belowbar | ✅     | Below bar location |
| location.bottom   | ✅     | Bottom location    |
| location.top      | ✅     | Top location       |

### Order

| Function         | Status | Description      |
|------------------|--------|------------------|
| order.ascending  | ✅     | Ascending order  |
| order.descending | ✅     | Descending order |

### Plot

| Function                    | Status | Description                 |
|-----------------------------|--------|-----------------------------|
| plot.linestyle_dashed       | 🔴     | Dashed line style           |
| plot.linestyle_dotted       | 🔴     | Dotted line style           |
| plot.linestyle_solid        | 🔴     | Solid line style            |
| plot.style_area             | ✅     | Area plot style             |
| plot.style_areabr           | ✅     | Area break plot style       |
| plot.style_circles          | ✅     | Circles plot style          |
| plot.style_columns          | ✅     | Columns plot style          |
| plot.style_cross            | ✅     | Cross plot style            |
| plot.style_histogram        | ✅     | Histogram plot style        |
| plot.style_line             | ✅     | Line plot style             |
| plot.style_linebr           | ✅     | Line break plot style       |
| plot.style_stepline         | ✅     | Stepline plot style         |
| plot.style_stepline_diamond | ✅     | Stepline diamond plot style |
| plot.style_steplinebr       | 🔴     | Stepline break plot style   |

### Position

| Function               | Status | Description            |
|------------------------|--------|------------------------|
| position.bottom_center | ✅     | Bottom center position |
| position.bottom_left   | ✅     | Bottom left position   |
| position.bottom_right  | ✅     | Bottom right position  |
| position.middle_center | ✅     | Middle center position |
| position.middle_left   | ✅     | Middle left position   |
| position.middle_right  | ✅     | Middle right position  |
| position.top_center    | ✅     | Top center position    |
| position.top_left      | ✅     | Top left position      |
| position.top_right     | ✅     | Top right position     |

### Scale

| Function    | Status | Description |
|-------------|--------|-------------|
| scale.left  | ✅     | Left scale  |
| scale.none  | ✅     | No scale    |
| scale.right | ✅     | Right scale |

### Settlement_as_close

| Function                    | Status | Description                 |
|-----------------------------|--------|-----------------------------|
| settlement_as_close.inherit | 🔴     | Inherit settlement as close |
| settlement_as_close.off     | 🔴     | Settlement as close off     |
| settlement_as_close.on      | 🔴     | Settlement as close on      |

### Shape

| Function           | Status | Description         |
|--------------------|--------|---------------------|
| shape.arrowdown    | ✅     | Arrow down shape    |
| shape.arrowup      | ✅     | Arrow up shape      |
| shape.circle       | ✅     | Circle shape        |
| shape.cross        | ✅     | Cross shape         |
| shape.diamond      | ✅     | Diamond shape       |
| shape.flag         | ✅     | Flag shape          |
| shape.labeldown    | ✅     | Label down shape    |
| shape.labelup      | ✅     | Label up shape      |
| shape.square       | ✅     | Square shape        |
| shape.triangledown | ✅     | Triangle down shape |
| shape.triangleup   | ✅     | Triangle up shape   |
| shape.xcross       | ✅     | X-cross shape       |

### Size

| Function    | Status | Description |
|-------------|--------|-------------|
| size.auto   | ✅     | Auto size   |
| size.huge   | ✅     | Huge size   |
| size.large  | ✅     | Large size  |
| size.normal | ✅     | Normal size |
| size.small  | ✅     | Small size  |
| size.tiny   | ✅     | Tiny size   |

### Splits

| Function           | Status | Description       |
|--------------------|--------|-------------------|
| splits.denominator | 🔴     | Split denominator |
| splits.numerator   | 🔴     | Split numerator   |

### Text

| Function           | Status | Description           |
|--------------------|--------|-----------------------|
| text.align_bottom  | ✅     | Bottom text alignment |
| text.align_center  | ✅     | Center text alignment |
| text.align_left    | ✅     | Left text alignment   |
| text.align_right   | ✅     | Right text alignment  |
| text.align_top     | ✅     | Top text alignment    |
| text.format_bold   | ✅     | Bold text format      |
| text.format_italic | ✅     | Italic text format    |
| text.format_none   | ✅     | No text format        |
| text.wrap_auto     | ✅     | Auto text wrap        |
| text.wrap_none     | ✅     | No text wrap          |

### Xloc

| Function       | Status | Description          |
|----------------|--------|----------------------|
| xloc.bar_index | ✅     | Bar index x-location |
| xloc.bar_time  | ✅     | Bar time x-location  |

### Yloc

| Function      | Status | Description          |
|---------------|--------|----------------------|
| yloc.abovebar | ✅     | Above bar y-location |
| yloc.belowbar | ✅     | Below bar y-location |
| yloc.price    | ✅     | Price y-location     |

### Alerts

| Function                      | Status | Description                        |
|-------------------------------|--------|------------------------------------|
| alert.freq_all                | ✅     | Alert frequency all                |
| alert.freq_once_per_bar       | ✅     | Alert frequency once per bar       |
| alert.freq_once_per_bar_close | ✅     | Alert frequency once per bar close |

### Backadjustment

| Function               | Status | Description            |
|------------------------|--------|------------------------|
| backadjustment.inherit | 🔴     | Inherit backadjustment |
| backadjustment.off     | 🔴     | Backadjustment off     |
| backadjustment.on      | 🔴     | Backadjustment on      |

### Barmerge

| Function               | Status | Description   |
|------------------------|--------|---------------|
| barmerge.gaps_off      | ✅     | Gaps off      |
| barmerge.gaps_on       | ✅     | Gaps on       |
| barmerge.lookahead_off | ✅     | Lookahead off |
| barmerge.lookahead_on  | ✅     | Lookahead on  |
