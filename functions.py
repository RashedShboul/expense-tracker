from datetime import datetime
import json
import os
import csv

FILE_PATH = 'expenses.json'
CSV_FILE_NAME = 'report.csv'

def save_expenses(expenses):
    # Save expenses to the json file after doing some operation
    with open(FILE_PATH, 'w') as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    # Read all expenses from their json file to do some operations on them
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def add_expense(description, amount):
    if amount < 0:
        print("Invalid amount. Please provide a positive number.")
        return
    new_exp = {
        'id': 1,
        'amount': amount,
        'description': description,
        'createdAt': str(datetime.now().replace(microsecond=0).isoformat())
    }
    all_expenses = load_expenses()
    if not all_expenses:
        new_exp['id'] = 1
    else:
        new_exp['id'] = max(item['id'] for item in all_expenses) + 1
    all_expenses.append(new_exp)
    save_expenses(all_expenses)
    expense_id = new_exp['id']
    print(f'Expense added with id {expense_id}')

def list_expenses():
    all_expenses = load_expenses()
    if all_expenses:
        for exp in all_expenses:
            expense_id, description, amount = exp['id'], exp['description'], exp['amount']
            print(f'{expense_id} | description: {description} | amount: {amount}')
    else:
        print('No expenses added yet')

def update_expense(target_id, new_description=None, new_amount=None):
    all_expenses = load_expenses()
    for exp in all_expenses:
        if exp['id'] == target_id:
            if new_description is not None:
                exp['description'] = new_description
            if new_amount is not None:
                if new_amount > 0:
                    exp['amount'] = new_amount
                else:
                    print("Invalid amount. Update aborted.")
                    return False
            save_expenses(all_expenses)
            print(f'Expense with ID {target_id} updated')
            return True
    print(f'Expense with ID {target_id} not found')
    return False

def delete_expense(target_id):
    all_expenses = load_expenses()
    initial_length = len(all_expenses)
    all_expenses = [exp for exp in all_expenses if exp['id'] != target_id]
    if len(all_expenses) < initial_length:
        save_expenses(all_expenses)
        print(f'Expense with ID {target_id} deleted')
        return True
    print(f'Expense with ID {target_id} not found')
    return False

def compute_total():
    all_expenses = load_expenses()
    return sum(item['amount'] for item in all_expenses)

def compute_monthly_total(month):
    all_expenses = load_expenses()
    return sum(exp['amount'] for exp in all_expenses if datetime.fromisoformat(exp['createdAt']).month == month)

def export_expenses_csv():
    all_expenses = load_expenses()
    data = [['ID', 'Description', 'Amount']]
    for exp in all_expenses:
        expense_id, description, amount = exp['id'], exp['description'], exp['amount']
        data.append([expense_id, description, amount])
    with open(CSV_FILE_NAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerows(data)
        csv_writer.writerow(['Sum', '', compute_total()])