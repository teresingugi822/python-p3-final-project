from database.setup import session
from models.product import Product
from models.supplier import Supplier
from models.transaction import Transaction
from sqlalchemy import func

def report_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. Inventory Summary")
        print("2. Supplier Product Count")
        print("3. Transactions Summary")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            inventory_summary()
        elif choice == "2":
            supplier_product_count()
        elif choice == "3":
            transactions_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def inventory_summary():
    print("\n--- Inventory Summary ---")
    products = session.query(Product).all()
    total = 0
    for p in products:
        print(f"Product: {p.name} | Quantity: {p.quantity}")
        total += p.quantity
    print(f"Total Units in Inventory: {total}")

def supplier_product_count():
    print("\n--- Supplier Product Count ---")
    results = (
        session.query(Supplier.name, func.count(Product.id))
        .join(Product, Supplier.id == Product.supplier_id)
        .group_by(Supplier.id)
        .all()
    )
    for name, count in results:
        print(f"Supplier: {name} | Products Supplied: {count}")

def transactions_summary():
    print("\n--- Transactions Summary ---")
    results = (
        session.query(Transaction.type, func.sum(Transaction.quantity))
        .group_by(Transaction.type)
        .all()
    )
    for trans_type, total_qty in results:
        print(f"Type: {trans_type.capitalize()} | Total Quantity: {total_qty}")
