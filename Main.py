from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. List Expenses")
        print("5. Categorize Expenses")
        print("6. Analyze Spending")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the expense name: ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            tracker.add_expense(name, amount, category)
        elif choice == "2":
            tracker.list_expenses()
            index = int(input("Enter the expense number to edit: ")) - 1
            name = input("Enter the new name (leave blank to keep current): ")
            amount = input("Enter the new amount (leave blank to keep current): ")
            category = input("Enter the new category (leave blank to keep current): ")
            tracker.edit_expense(index, name=name or None, amount=float(amount) if amount else None, category=category or None)
        elif choice == "3":
            tracker.list_expenses()
            index = int(input("Enter the expense number to delete: ")) - 1
            tracker.delete_expense(index)
        elif choice == "4":
            tracker.list_expenses()
        elif choice == "5":
            tracker.categorize_expenses()
        elif choice == "6":
            tracker.analyze_spending()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
