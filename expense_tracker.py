import csv
import datetime

expenses = []
categories = []


def add_expense():
    date_str = input("Enter the expense date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in the correct format (YYYY-MM-DD).")
        return

    category = input("Enter the expense category: ").lower()

    if category not in categories:
        add_category(category)

    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    print("Expense added successfully!")


def add_category(category):
    if category not in categories:
        categories.append(category)
        print(f"Category '{category}' added successfully!")
    else:
        print(f"Category '{category}' already exists!")


def print_expenses(expenses):
    print("ID  Date        Category       Description       Amount")
    print("---------------------------------------------------------")
    for i, expense in enumerate(expenses, start=1):
        date_str = expense["date"].strftime("%Y-%m-%d")
        category = expense["category"]
        description = expense["description"]
        amount = expense["amount"]
        print(f"{i:<4}{date_str:<12}{category:<15}{description:<18}{amount:.2f}")


def view_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        print("Expense List:")
        print("-------------")
        print_expenses(expenses)


def filter_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("Filter Expenses:")
    print("1. Filter by Date Range")
    print("2. Filter by Category")
    print("3. Filter by Date Range and Category")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        filter_by_date_range()
    elif choice == "2":
        filter_by_category()
    elif choice == "3":
        filter_by_date_range_and_category()
    else:
        print("Invalid choice. Please try again.")


def filter_by_date_range():
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the dates in the correct format (YYYY-MM-DD).")
        return

    filtered_expenses = [
        expense for expense in expenses
        if start_date <= expense["date"] <= end_date
    ]

    if not filtered_expenses:
        print("No expenses found within the specified date range.")
    else:
        print("Filtered Expense List:")
        print("------------------")
        print_expenses(filtered_expenses)


def filter_by_category():
    category = input("Enter the category: ")
    if category not in categories:
        print("Category not found.")
        return

    filtered_expenses = [
        expense for expense in expenses
        if expense["category"] == category
    ]

    if not filtered_expenses:
        print("No expenses found for the specified category.")
    else:
        print("Filtered Expense List:")
        print("------------------")
        print_expenses(filtered_expenses)


def filter_by_date_range_and_category():
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the dates in the correct format (YYYY-MM-DD).")
        return

    category = input("Enter the category: ")
    if category not in categories:
        print("Category not found.")
        return

    filtered_expenses = [
        expense for expense in expenses
        if start_date <= expense["date"] <= end_date and expense["category"] == category
    ]

    if not filtered_expenses:
        print("No expenses found for the specified date range and category.")
    else:
        print("Filtered Expense List:")
        print("------------------")
        print_expenses(filtered_expenses)


def calculate_total_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("Calculate Total Expenses:")
    print("1. Calculate total for all expenses")
    print("2. Calculate total within a date range")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        total_expenses = sum(expense["amount"] for expense in expenses)
        print(f"Total Expenses: {total_expenses}")
    elif choice == "2":
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the dates in the correct format (YYYY-MM-DD).")
            return

        total_expenses = sum(
            expense["amount"]
            for expense in expenses
            if start_date <= expense["date"] <= end_date
        )
        print(f"Total Expenses within {start_date_str} and {end_date_str}: {total_expenses}")
    else:
        print("Invalid choice. Please try again.")


def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()
    expense_id = int(input("Enter the expense ID to delete: "))
    if expense_id < 1 or expense_id > len(expenses):
        print("Invalid expense ID. Please try again.")
        return

    del expenses[expense_id - 1]
    print("Expense deleted successfully!")
    print_expenses(expenses)


def export_expense_data():
    if not expenses:
        print("No expenses found.")
        return

    file_name = input("Enter the file name to export (e.g., expenses.csv): ")
    if not file_name.endswith(".csv"):
        print("Invalid file name. The file must be in CSV format.")
        return

    try:
        with open(file_name, "w", newline="") as csvfile:
            fieldnames = ["Date", "Category", "Description", "Amount"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in expenses:
                writer.writerow({
                    "Date": expense["date"].strftime("%Y-%m-%d"),
                    "Category": expense["category"],
                    "Description": expense["description"],
                    "Amount": expense["amount"],
                })

        print(f"Expense data exported to {file_name} successfully!")
    except IOError:
        print("An error occurred while exporting the expense data.")


def main():
    while True:
        print("\nExpense Tracker")
        print("---------------")
        print("1. Add an Expense")
        print("2. View Expense List")
        print("3. Filter Expenses")
        print("4. Calculate Total Expenses")
        print("5. Delete an Expense")
        print("6. Export Expense Data")
        print("7. Add categories")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print("Enter expense details:")
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            export_expense_data()
        elif choice == "7":
            category = input("Enter the new category: ").lower()
            add_category(category)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()
