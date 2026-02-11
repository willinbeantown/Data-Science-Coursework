# MODULE 2 - Python Review


## The Python Language

- Python, a newer, high-level language best used for programs using mathematics.


Usage Notes for Scripting on a Windows:

- On the PC, use `Anaconda Prompt` to access Python.


## Expressions

- Remember the **order of operations** (M-D-A-S)

- Addition `+`

- Subtraction `-`

- Multiplication `*`

- Division `/`

- Modulus `%` - The remainder from a division

- Exponents `**` - To cube would be `4 ** 3`

- Each expression can be combined with a `=` for expressions like `+=` and `-=`

- `//=` - Floor division (the other side of modulus), *5//2 = 2*, *5%2 = 1*


## Data Types

- Floats (0.00, 18302.48205) - `float()` (aka 'real' in some programming languages)

- Integers (7, 22, -42) - `int()`

- Strings ('yes', '3821397', 'a collection of characters') - `str()`

- Boolean (True or False) - `bool()`

- Tuples (ordered, immutable, indexed, duplicates okay) - `("may", "june", "june")`

- Sets (unordered, unindexed, unique values) - `{"may", "june"}`

- Lists (ordered, mutable, indexed, duplicates ok) - `["may", "june", "june"]`

- Dictionary (unordered, mutable, indexed, no duplicates) - `{"may": "month", "june": "month"}`


## Relational Operators

| Operator | Name |
|-|-|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `<` | Less than |
| `<=` | Less than or equal to |


## Membership Operators

- Testing to see if a value is in a `list`, `tuple`, or 'string'

| Operator | Description |
|-|-|
| `in` | Returns True if a sequence is in the object |
| `not in` | Returns True of a sequence is not present |


## Logical Operators

| Operator | Description |
|-|-|
| `and` | Returns True if both are true |
| `or` | Returns true if 1 is true |
| `not` | Reverse Result, Returns False if result is True |


## Python Control Flows

- Sequential, line by line.

- Iteration -> `for` & `while`

  - For loops iterates over a sequence (list, tuple, dict, set, str)

- Branching (if, else...)


## Pythong Function

- **User defined functions** are created by the developer to use in addition to *built-in functions*, such as `int()`, `range()`, and `input()`

- **Fruitful Function** returns a value (`sum()`)

- **Void Function**, or a *Procedure Function*, performs a task (`pint()`)
