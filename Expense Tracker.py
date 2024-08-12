import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        date = datetime.date.today()
        new_expense = Expense(name, amount, category, date)
        self.expenses.append(new_expense)
        print(f"Added: {new_expense}")

    def edit_expense(self, index, name=None, amount=None, category=None):
        if index < len(self.expenses):
            if name:
                self.expenses[index].name = name
            if amount:
                self.expenses[index].amount = amount
            if category:
                self.expenses[index].category = category
            print(f"Edited: {self.expenses[index]}")
        else:
            print("Expense not found.")

    def delete_expense(self, index):
        if index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Deleted: {removed_expense}")
        else:
            print("Expense not found.")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for i, expense in enumerate(self.expenses):
            print(f"{i + 1}. {expense}")

    def categorize_expenses(self):
        categorized = {}
        for expense in self.expenses:
            if expense.category not in categorized:
                categorized[expense.category] = 0
            categorized[expense.category] += expense.amount
        for category, total in categorized.items():
            print(f"{category}: ${total}")

    def analyze_spending(self):
        total_spent = sum(expense.amount for expense in self.expenses)
        print(f"Total Spent: ${total_spent}")
        self.categorize_expenses()
