---
layout: default
title: Strategy
parent: API Coverage
nav_order: 27
---

## Strategy

### Declaration
| Function     | Status | Description                                    |
|--------------|--------|------------------------------------------------|
| strategy()   | ✅     | Strategy declaration (title, overlay, qty, etc.) |

### Order Functions
| Function                | Status | Description                              |
|-------------------------|--------|------------------------------------------|
| strategy.entry()        | ✅     | Submit entry order (via CTrade)           |
| strategy.close()        | ✅     | Close position by entry ID               |
| strategy.close_all()    | ✅     | Close all open positions                 |
| strategy.exit()         | ✅     | Set SL/TP exit (via PositionModify)      |
| strategy.order()        | ✅     | Submit generic order                     |
| strategy.cancel()       | ✅     | Cancel pending order by ID               |
| strategy.cancel_all()   | ✅     | Cancel all pending orders                |

### Properties
| Function                       | Status | Description                         |
|--------------------------------|--------|-------------------------------------|
| strategy.position_size         | ✅     | Current position size               |
| strategy.position_avg_price    | ✅     | Average entry price                 |
| strategy.equity                | ✅     | Account equity                      |
| strategy.openprofit            | ✅     | Unrealized P&L                      |
| strategy.netprofit             | ✅     | Net profit                          |
| strategy.initial_capital       | ✅     | Starting capital                    |
| strategy.closedtrades          | ✅     | Number of closed trades             |
| strategy.opentrades            | ✅     | Number of open trades               |
| strategy.wintrades             | ✅     | Number of winning trades            |
| strategy.losstrades            | ✅     | Number of losing trades             |
| strategy.grossprofit           | 🔵     | Gross profit                        |
| strategy.grossloss             | 🔵     | Gross loss                          |
| strategy.max_drawdown          | 🔵     | Maximum drawdown                    |

### Constants
| Function         | Status | Description     |
|------------------|--------|-----------------|
| strategy.long    | ✅     | Long direction  |
| strategy.short   | ✅     | Short direction |

### Trade History Functions
| Function                             | Status | Description                      |
|--------------------------------------|--------|----------------------------------|
| strategy.closedtrades.entry_bar_index() | 🔵  | Entry bar of closed trade        |
| strategy.closedtrades.entry_price()  | 🔵     | Entry price of closed trade      |
| strategy.closedtrades.entry_id()     | 🔵     | Entry ID of closed trade         |
| strategy.closedtrades.exit_bar_index()  | 🔵  | Exit bar of closed trade         |
| strategy.closedtrades.exit_price()   | 🔵     | Exit price of closed trade       |
| strategy.closedtrades.exit_id()      | 🔵     | Exit ID of closed trade          |
| strategy.closedtrades.profit()       | 🔵     | Profit of closed trade           |
| strategy.closedtrades.size()         | 🔵     | Size of closed trade             |
| strategy.closedtrades.commission()   | 🔵     | Commission of closed trade       |
| strategy.opentrades.entry_bar_index()   | 🔵  | Entry bar of open trade          |
| strategy.opentrades.entry_price()    | 🔵     | Entry price of open trade        |
| strategy.opentrades.entry_id()       | 🔵     | Entry ID of open trade           |
| strategy.opentrades.profit()         | 🔵     | Profit of open trade             |
| strategy.opentrades.size()           | 🔵     | Size of open trade               |
