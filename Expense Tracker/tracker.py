import csv
import os
from expense import Expense


class ExpenseTracker:

    def __init__(self):
        self.transactions = []
        self.filename = "transactions.csv"
        self.load_transactions()


    # -----------------------------
    # Load Transactions
    # -----------------------------
    def load_transactions(self):

        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", newline="") as file:

                reader = csv.reader(file)
                next(reader, None)

                for row in reader:

                    if len(row) == 4:

                        transaction = Expense(
                            row[0],
                            row[1],
                            float(row[2]),
                            row[3]
                        )

                        self.transactions.append(transaction)

        except Exception as e:
            print("Error loading transactions:", e)



    # -----------------------------
    # Save Transactions
    # -----------------------------
    def save_transactions(self):

        try:
            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Transaction ID",
                    "Type",
                    "Amount",
                    "Category"
                ])

                for transaction in self.transactions:

                    writer.writerow([
                        transaction._trans_id,
                        transaction.get_transaction_type(),
                        transaction._amount,
                        transaction._category
                    ])

        except Exception as e:
            print("Error saving transactions:", e)



    # -----------------------------
    # Add Income
    # -----------------------------
    def add_income(self):

        try:

            print("\nEnter Income Details")
            print("-" * 40)

            trans_id = input("Transaction ID : ")
            amount = float(input("Amount         : ₹"))
            category = input("Category       : ")


            transaction = Expense(
                trans_id,
                "Income",
                amount,
                category
            )

            self.transactions.append(transaction)

            self.save_transactions()

            print("\nIncome added successfully.")

        except ValueError:
            print("\nInvalid amount entered.")



    # -----------------------------
    # Add Expense
    # -----------------------------
    def add_expense(self):

        try:

            print("\nEnter Expense Details")
            print("-" * 40)

            trans_id = input("Transaction ID : ")
            amount = float(input("Amount         : ₹"))
            category = input("Category       : ")


            transaction = Expense(
                trans_id,
                "Expense",
                amount,
                category
            )

            self.transactions.append(transaction)

            self.save_transactions()

            print("\nExpense added successfully.")

        except ValueError:
            print("\nInvalid amount entered.")



    # -----------------------------
    # Display Transactions
    # -----------------------------
    def display_transactions(self):

        if not self.transactions:
            print("\nNo transactions available.")
            return


        print("\n" + "=" * 70)

        print("{:<12}{:<12}{:<15}{:<20}".format(
            "ID",
            "TYPE",
            "AMOUNT",
            "CATEGORY"
        ))

        print("=" * 70)


        for transaction in self.transactions:

            print("{:<12}{:<12}{:<15.2f}{:<20}".format(
                transaction._trans_id,
                transaction.get_transaction_type(),
                transaction._amount,
                transaction._category
            ))

        print("=" * 70)



    # -----------------------------
    # Search Transaction
    # -----------------------------
    def search_transaction(self):

        trans_id = input("\nEnter Transaction ID: ")


        for transaction in self.transactions:

            if transaction._trans_id == trans_id:

                transaction.display()
                return


        print("\nTransaction not found.")



    # -----------------------------
    # Monthly Summary
    # -----------------------------
    def monthly_summary(self):

        income = 0
        expense = 0


        for transaction in self.transactions:

            if transaction.get_transaction_type() == "Income":
                income += transaction._amount

            else:
                expense += transaction._amount



        print("\n" + "=" * 45)
        print("          MONTHLY SUMMARY")
        print("=" * 45)

        print(f"Total Income  : ₹{income:.2f}")
        print(f"Total Expense : ₹{expense:.2f}")
        print(f"Net Balance   : ₹{income-expense:.2f}")

        print("=" * 45)