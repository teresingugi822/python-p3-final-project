from database.setup import initialize_database
import os

def database_menu():
    while True:
        print("\n--- Database Menu ---")
        print("1. Initialize Database")
        print("2. Delete Database")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            initialize_database()
            print("Database initialized.")
        elif choice == "2":
            if os.path.exists("inventory.db"):
                os.remove("inventory.db")
                print("Database deleted.")
            else:
                print("No database file found.")
        elif choice == "3":
            break
        else:
            print("Invalid option.")
