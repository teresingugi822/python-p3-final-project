from database.setup import session
from models.transaction import Transaction
from models.product import Product

def transaction_menu():
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def add_transaction():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    trans_type = input("Enter type ('in' or 'out'): ").lower()

    product = session.query(Product).get(product_id)
    if not product:
        print("Product not found.")
        return

    if trans_type == "out" and product.quantity < quantity:
        print("Insufficient product quantity.")
        return

    transaction = Transaction(product_id=product_id, quantity=quantity, type=trans_type)
    session.add(transaction)

    if trans_type == "in":
        product.quantity += quantity
    elif trans_type == "out":
        product.quantity -= quantity

    session.commit()
    print("Transaction recorded.")

def view_transactions():
    transactions = session.query(Transaction).all()
    for t in transactions:
        print(f"ID: {t.id} | Product ID: {t.product_id} | Type: {t.type} | Quantity: {t.quantity} | Time: {t.timestamp}")
