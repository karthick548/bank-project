import os
import sys

def main_menu():
    while True:
        print("\n==============================")
        print("  Welcome to My Bank  ")
        print("==============================")
        print("1. New User Registration")
        print("2. Set ATM PIN")
        print("3. Access ATM")
        print("4. Exit")

        try:
            choice = int(input("Select your option (1-4): ").strip())
        except ValueError:
            print("⚠ Please enter a valid number (1-4).")
            continue

        if choice == 1:
            os.system(f"{sys.executable} user.py")
        elif choice == 2:
            os.system(f"{sys.executable} pincreation.py")
        elif choice == 3:
            os.system(f"{sys.executable} atmmachine.py")
        elif choice == 4:
            print("\nThank you for visiting My Bank. Goodbye!")
            break
        else:
            print("⚠ Invalid option! Please select a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
