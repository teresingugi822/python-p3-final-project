from cli.product_commands import product_menu
from cli.supplier_commands import supplier_menu
from cli.transaction_commands import transaction_menu
from cli.report_commands import report_menu
from cli.database_commands import database_menu

def main_menu():
    while True:
        print("\n===== Inventory Management CLI =====")
        print("1. Product Menu")
        print("2. Supplier Menu")
        print("3. Transaction Menu")
        print("4. Reports Menu")
        print("5. Database Options")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            product_menu()
        elif choice == "2":
            supplier_menu()
        elif choice == "3":
            transaction_menu()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            database_menu()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")
