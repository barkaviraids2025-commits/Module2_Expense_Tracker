# Expense Tracker (Module 02 - Python Mini Project)

A simple command-line app to track daily expenses. Data is saved in `expenses.json`, so it is still there next time you run it.

**Author:** Barkavi R

## Features

- Add an expense with title, amount and category
- View all expenses in a table with the total
- See spending by category (with percentages)
- Delete a wrong entry
- Input checking, so wrong values do not crash the program
- Auto-save to a JSON file

## Python concepts used

| Concept | Where it is used |
|---|---|
| Variables and data types | amounts (float), titles (str), dates |
| Lists and dictionaries | each expense is a dictionary stored in a list |
| Loops | menu loop, printing the table, category totals |
| Functions | one function per feature |
| File handling and JSON | `load_expenses()` and `save_expenses()` |
| Error handling (`try/except`) | invalid amounts, missing file |

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download or clone this repo.
3. In a terminal inside the folder, run:

```bash
python expense_tracker.py
```

## Sample output

```
===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
3. Category summary
4. Delete an expense
5. Exit
Choose an option (1-5): 3

Spending by category:
  Food         Rs    230.00  (58%)
  Travel       Rs    120.00  (30%)
  Bills        Rs     50.00  (12%)

Highest category: Food
```

## Future ideas

- Monthly budget limit with a warning
- Export to CSV or Excel
- Simple GUI using Tkinter
