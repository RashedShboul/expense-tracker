# Expense Tracker

A simple command-line application to track your expenses. This project allows you to add, update, delete, list, and summarize expenses, with data stored in a JSON file. You can also export your expenses to a CSV file.
This is a learning project from: https://roadmap.sh/projects/expense-tracker

## Features

- Add a new expense with a description and amount.
- Update an existing expense by its ID.
- Delete an expense by its ID.
- List all expenses.
- View a summary of total expenses or filter by month.
- Export expenses to a CSV file.

## Requirements

- Python 3.7 or higher.

## Installation

1. Clone this repository or download the script files.
2. Ensure you have Python 3.7+ installed on your system.
3. No additional dependencies are required beyond Python’s standard library.

## Usage

Run the script with the following commands:

### Add Expense
```bash
python expense-tracker.py add -d "Grocery shopping" -a 150.50
```
### delete Expense 
```bash
python expense-tracker.py delete --id 1
```
### Update Expense
```bash
python expense-tracker.py update --id 1 -d "New description" -a 175.00
python expense-tracker.py update --id 1 -d "New description"
python expense-tracker.py update --id 1 -a 100.9
```
### List all expenses
```bash
python expense-tracker.py list
```
### Summary
```bash
python expense-tracker.py summary
```

### Summary for a specific month
```bash
python expense-tracker.py summary -m 9
```
### Export Expenses to CSV
```bash
python expense-tracker.py export
```
