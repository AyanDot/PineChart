---
layout: default
title: User-Defined Types
parent: API Coverage
nav_order: 29
---

## User-Defined Types

| Feature                    | Status | Description                              |
|----------------------------|--------|------------------------------------------|
| `type` declaration         | ✅     | UDT definition with fields               |
| `TypeName.new()`           | ✅     | Construction (positional + named args)    |
| Field access `obj.field`   | ✅     | Dot notation (chained: `rect.topLeft.x`) |
| Field assignment `:=`      | ✅     | With `:=`, `+=`, `-=`, `*=`, `/=`        |
| `var` persistence          | ✅     | UDT instances persist across bars         |
| `na` handling              | ✅     | `na` assignment and `na()` detection      |
| `obj.copy()`               | ✅     | Shallow copy                             |
| Method calls               | ✅     | `obj.method(args)` → `method(obj, args)` |
| `array<UDT>` fields        | 🔵     | Array of UDT or arrays inside UDTs       |
| `for obj in array<UDT>`    | 🔵     | UDT array iteration                      |
