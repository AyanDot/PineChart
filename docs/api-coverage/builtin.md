---
layout: default
title: Builtin
parent: API Coverage
nav_order: 2
---

## Builtin

### Variables

| Function        | Status  | Description                            |
|-----------------|---------|----------------------------------------|
| bar_index       | ✅      | Current bar index                      |
| close           | ✅      | Close price                            |
| high            | ✅      | High price                             |
| hl2             | ✅      | Average of high and low                |
| hlc3            | ✅      | Average of high, low, and close        |
| hlcc4           | ✅      | Average of high, low, close, and close |
| last_bar_index  | ✅      | Index of last bar                      |
| last_bar_time   | ✅      | Time of last bar                       |
| low             | ✅      | Low price                              |
| na              | ✅      | Not a number (NaN) literal             |
| ohlc4           | ✅      | Average of open, high, low, and close  |
| open            | ✅      | Open price                             |
| timenow         | ✅      | Current time                           |
| volume          | ✅      | Volume                                 |
| ask             | 🔵      | Ask price                              |
| bid             | 🔵      | Bid price                              |
| dayofmonth      | ✅      | Day of month                           |
| dayofweek       | ✅      | Day of week                            |
| hour            | ✅      | Hour                                   |
| minute          | ✅      | Minute                                 |
| month           | ✅      | Month                                  |
| second          | ✅      | Second                                 |
| time            | ✅      | Bar time                               |
| time_close      | ✅      | Bar close time                         |
| time_tradingday | 🔵      | Trading day time                       |
| weekofyear      | ✅      | Week of year                           |
| year            | ✅      | Year                                   |


### Constants

| Function | Status | Description   |
|----------|--------|---------------|
| false    | ✅      | Boolean false |
| true     | ✅      | Boolean true  |


### Functions

| Function         | Status | Description           |
|------------------|--------|-----------------------|
| indicator()      | ✅      | Indicator declaration |
| input()          | ✅      | Input parameter (returns defval) |
| na()             | ✅      | Check if value is NaN |
| nz()             | ✅      | Replace NaN with zero |
| alert()          | 🔵      | Alert function        |
| alertcondition() | 🔵      | Alert condition       |
| bool()           | ✅      | Boolean conversion    |
| box()            | ✅      | Box object (via handle system) |
| color()          | ✅      | Color type cast       |
| dayofmonth()     | ✅      | Day of month function |
| dayofweek()      | ✅      | Day of week function  |
| fill()           | ✅      | Fill between plots/hlines (solid & gradient) |
| fixnan()         | ✅      | Fix NaN values        |
| float()          | ✅      | Float conversion      |
| hline()          | ✅      | Horizontal line (via DrawingStore) |
| hour()           | ✅      | Hour function         |
| int()            | ✅      | Integer conversion    |
| label()          | ✅      | Label object (via handle system) |
| library()        | 🔵      | Library declaration   |
| line()           | ✅      | Line object (via handle system) |
| linefill()       | 🔵      | Linefill object       |
| max_bars_back()  | 🔵      | Maximum bars back     |
| minute()         | ✅      | Minute function       |
| month()          | ✅      | Month function        |
| second()         | ✅      | Second function       |
| strategy()       | ✅      | Strategy declaration (parsed, maps to CTrade) |
| string()         | ✅      | String conversion     |
| table()          | ✅      | Table object (via handle system) |
| time()           | ✅      | Time function         |
| time_close()     | ✅      | Time close function   |
| timestamp()      | ✅      | Timestamp function    |
| weekofyear()     | ✅      | Week of year function |
| year()           | ✅      | Year function         |
| runtime.error()  | ✅      | Runtime error (halts execution) |
