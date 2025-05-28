from sqlalchemy import Column, Integer, String, ForeignKey
from models import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    def __repr__(self):
        return f"<Product(name={self.name}, quantity={self.quantity})>"
