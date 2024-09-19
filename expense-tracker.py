import argparse
from functions import add_expense, list_expenses, update_expense, delete_expense, compute_total, compute_monthly_total, export_expenses_csv

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("-d", "--description", required=True, help="Expense description")
    add_parser.add_argument("-a", "--amount", type=float, required=True, help="Expense amount")

    # Update expense
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", type=int, required=True, help="Expense ID")
    update_parser.add_argument("-d", "--description", help="New expense description")
    update_parser.add_argument("-a", "--amount", type=float, help="New expense amount")

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID to delete")

    # List expenses
    subparsers.add_parser("list", help="List all expenses")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="View summary of expenses")
    summary_parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Month (1-12) for monthly summary")

    # Export
    export_parser = subparsers.add_parser("export", help="Export expenses to a csv file")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "update":
        if args.description is not None and args.amount is not None:
            update_expense(args.id, args.description, args.amount)
        elif args.description is not None:
            update_expense(args.id, args.description, None)
        elif args.amount is not None:
            update_expense(args.id, None, args.amount)
        else:
            print('Provide new description and/or new amount')
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        if not args.month:
            print(compute_total())
        else:
            print(compute_monthly_total(args.month))
    elif args.command == "export":
        export_expenses_csv()

if __name__ == "__main__":
    main()