from database.setup import session
from models.supplier import Supplier

def supplier_menu():
    while True:
        print("\n--- Supplier Menu ---")
        print("1. Add Supplier")
        print("2. View All Suppliers")
        print("3. Delete Supplier")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_supplier()
        elif choice == "2":
            view_suppliers()
        elif choice == "3":
            delete_supplier()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def add_supplier():
    name = input("Enter supplier name: ")
    contact = input("Enter contact info: ")
    supplier = Supplier(name=name, contact_info=contact)
    session.add(supplier)
    session.commit()
    print("Supplier added.")

def view_suppliers():
    suppliers = session.query(Supplier).all()
    for s in suppliers:
        print(f"ID: {s.id} | Name: {s.name} | Contact: {s.contact_info}")

def delete_supplier():
    supplier_id = int(input("Enter supplier ID to delete: "))
    supplier = session.query(Supplier).get(supplier_id)
    if supplier:
        session.delete(supplier)
        session.commit()
        print("Supplier deleted.")
    else:
        print("Supplier not found.")
