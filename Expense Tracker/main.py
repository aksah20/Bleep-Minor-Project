import os
from tracker import ExpenseTracker


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    clear_screen()
    print("=" * 70)
    print("                    EXPENSE TRACKER SYSTEM")
    print("=" * 70)
    
    print("-" * 70)


def show_menu():
    print("\n                     MAIN MENU\n")
    print("  [1] Add Income")
    print("  [2] Add Expense")
    print("  [3] Display Transactions")
    print("  [4] Search Transaction")
    print("  [5] Monthly Summary")
    print("  [6] Exit")
    print("-" * 70)


def pause():
    input("\nPress Enter to continue...")


def main():

    tracker = ExpenseTracker()

    while True:

        header()
        show_menu()

        try:
            choice = int(input("Select an option (1-6): "))

            if choice == 1:
                header()
                print("ADD INCOME")
                print("-" * 70)
                tracker.add_income()
                pause()

            elif choice == 2:
                header()
                print("ADD EXPENSE")
                print("-" * 70)
                tracker.add_expense()
                pause()

            elif choice == 3:
                header()
                print("ALL TRANSACTIONS")
                print("-" * 70)
                tracker.display_transactions()
                pause()

            elif choice == 4:
                header()
                print("SEARCH TRANSACTION")
                print("-" * 70)
                tracker.search_transaction()
                pause()

            elif choice == 5:
                header()
                print("MONTHLY SUMMARY")
                print("-" * 70)
                tracker.monthly_summary()
                pause()

            elif choice == 6:
                clear_screen()

                print("=" * 70)
                print("            THANK YOU FOR USING EXPENSE TRACKER")
                print("=" * 70)
                print("\nExpense Tracker System")
            
                print("\nHAVE A GOOD DAY")
                print("=" * 70)

                break

            else:
                print("\nInvalid choice!")
                pause()

        except ValueError:
            print("\nPlease enter a valid number.")
            pause()


if __name__ == "__main__":
    main()