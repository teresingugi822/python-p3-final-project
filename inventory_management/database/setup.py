from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///inventory.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def initialize_database():
    from models.product import Product
    from models.supplier import Supplier
    from models.transaction import Transaction
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")
