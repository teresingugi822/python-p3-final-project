from database.setup import session
from models.product import Product
from models.supplier import Supplier

def product_menu():
    while True:
        print("\n--- Product Menu ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product_quantity()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    supplier_id = int(input("Enter supplier ID: "))
    product = Product(name=name, quantity=quantity, supplier_id=supplier_id)
    session.add(product)
    session.commit()
    print("Product added successfully.")

def view_products():
    products = session.query(Product).all()
    for p in products:
        print(f"ID: {p.id} | Name: {p.name} | Quantity: {p.quantity} | Supplier ID: {p.supplier_id}")

def update_product_quantity():
    product_id = int(input("Enter product ID: "))
    product = session.query(Product).get(product_id)
    if product:
        new_qty = int(input("Enter new quantity: "))
        product.quantity = new_qty
        session.commit()
        print("Quantity updated.")
    else:
        print("Product not found.")

def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted.")
    else:
        print("Product not found.")
