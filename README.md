# 📦 Inventory Management System (CLI)

This is a Command-Line Interface (CLI) application built with Python that helps users manage an inventory of products, suppliers, and transactions. The system supports operations like adding, viewing, updating, and deleting records, as well as generating summary reports.

---

## 🔧 Features

- Add, view, update, and delete **products**
- Manage **suppliers** and their contact info
- Record **inventory transactions** (in/out)
- Generate **summary reports** for inventory and transactions
- Uses **SQLAlchemy ORM** for database interaction
- Built with a **modular package structure**
- Easy to navigate **CLI interface**

---

## 🗃️ Technologies Used

- Python 3
- SQLAlchemy ORM
- SQLite (for the local database)
- Pipenv (for dependency management)

---

## 📁 Project Structure

inventory_management/
│
├── cli/ # Modular CLI commands
│ ├── main.py
│ ├── product_commands.py
│ ├── supplier_commands.py
│ ├── transaction_commands.py
│ ├── database_commands.py
│ └── report_commands.py
│
├── models/ # SQLAlchemy models
│ ├── product.py
│ ├── supplier.py
│ └── transaction.py
│
├── database/ # Database setup logic
│ └── setup.py
│
├── app.py # Application entry point
├── Pipfile # Pipenv config
├── Pipfile.lock
└── README.md

yaml
Copy
Edit
