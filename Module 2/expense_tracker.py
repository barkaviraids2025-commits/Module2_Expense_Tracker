"""
Expense Tracker - Module 02 Python Mini Project
Track daily expenses, see totals by category, and keep data saved in a file.
"""

import json
from datetime import date

FILE_NAME = "expenses.json"
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Education", "Other"]


def load_expenses():
    """Read saved expenses from the file (empty list if none yet)."""
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """Write all expenses to the file."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=2)


def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Amount (Rs): "))
            if amount > 0:
                return amount
            print("Amount must be more than 0.")
        except ValueError:
            print("Please enter a number, e.g. 150 or 49.5")


def choose_category():
    """Show the category menu and return the chosen one."""
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Choose category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice, try again.")


def add_expense(expenses):
    title = input("What did you spend on? ").strip() or "Untitled"
    amount = get_amount()
    category = choose_category()
    expenses.append({
        "date": str(date.today()),
        "title": title,
        "amount": amount,
        "category": category,
    })
    save_expenses(expenses)
    print(f"Added: {title} - Rs {amount:.2f} ({category})")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print(f"\n{'No':<4}{'Date':<12}{'Title':<20}{'Category':<12}{'Amount':>10}")
    print("-" * 58)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4}{e['date']:<12}{e['title'][:18]:<20}{e['category']:<12}{e['amount']:>10.2f}")
    print("-" * 58)
    print(f"{'Total':<48}{sum(e['amount'] for e in expenses):>10.2f}")


def category_summary(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())
    print("\nSpending by category:")
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<12} Rs {amt:>9.2f}  ({amt / grand_total * 100:.0f}%)")
    print(f"\nHighest category: {max(totals, key=totals.get)}")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    choice = input("Enter number to delete (or press Enter to cancel): ")
    if choice.isdigit() and 1 <= int(choice) <= len(expenses):
        removed = expenses.pop(int(choice) - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['title']}")
    else:
        print("Cancelled.")


def main():
    expenses = load_expenses()
    menu = """
===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
3. Category summary
4. Delete an expense
5. Exit"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Bye! Keep tracking your money.")
            break
        else:
            print("Please choose 1 to 5.")


if __name__ == "__main__":
    main()
