# Expense Tracker System

## Project Description

The Expense Tracker System is a console-based Python application developed using Object-Oriented Programming (OOP) concepts. It allows users to record income and expenses, search transactions, display all records, and generate a monthly financial summary.

All transaction data is stored in a CSV file to ensure persistence.

---

## Features

- Add Income
- Add Expense
- Display All Transactions
- Search Transaction
- Monthly Summary
- Save Records to CSV
- Load Records Automatically
- Exception Handling

---

## OOP Concepts Used

### Classes and Objects
- Transaction
- Expense
- ExpenseTracker

### Encapsulation
- Private attribute `__trans_type`
- Getter and Setter methods

### Inheritance
- Expense inherits from Transaction

### Abstraction
- Transaction is an abstract class using the `abc` module.

### File Handling
- Reads and writes transaction data using CSV files.

### Exception Handling
- Handles invalid input.
- Handles file-related errors.

---

## Files

- main.py
- transaction.py
- expense.py
- tracker.py
- transactions.csv
- README.md

---

## How to Run

```bash
python main.py
```

---

## Author
Anunay Kumar