import os
from hospital import Hospital


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    clear_screen()
    print("=" * 70)
    print("          HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM")
    print("=" * 70)
    
    print("-" * 70)


def show_menu():
    print("\n                    MAIN MENU\n")
    print("  [1] Register New Patient")
    print("  [2] Display All Patients")
    print("  [3] Search Patient")
    print("  [4] Update Patient Record")
    print("  [5] Delete Patient Record")
    print("  [6] Exit")
    print("-" * 70)


def pause():
    input("\nPress Enter to continue...")


def main():

    hospital = Hospital()

    while True:

        header()
        show_menu()

        try:
            choice = int(input("Select an option (1-6): "))

            if choice == 1:
                header()
                print("REGISTER NEW PATIENT")
                print("-" * 70)
                hospital.add_patient()
                pause()

            elif choice == 2:
                header()
                print("ALL PATIENT RECORDS")
                print("-" * 70)
                hospital.display_patients()
                pause()

            elif choice == 3:
                header()
                print("SEARCH PATIENT")
                print("-" * 70)
                hospital.search_patient()
                pause()

            elif choice == 4:
                header()
                print("UPDATE PATIENT RECORD")
                print("-" * 70)
                hospital.update_patient()
                pause()

            elif choice == 5:
                header()
                print("DELETE PATIENT RECORD")
                print("-" * 70)
                hospital.delete_patient()
                pause()

            elif choice == 6:
                clear_screen()
                print("=" * 70)
                print("        THANK YOU FOR USING OUR SYSTEM")
                print("=" * 70)
                print("\nHospital Patient Record Management System")
                
                print("\nHAVE A GOOD DAY")
                print("=" * 70)
                break

            else:
                print("\nInvalid choice! Please select between 1 and 6.")
                pause()

        except ValueError:
            print("\nInvalid input! Please enter a number.")
            pause()


if __name__ == "__main__":
    main()