from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
import datetime

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    type = Column(String)  # 'in' or 'out'
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Transaction(product_id={self.product_id}, type={self.type}, quantity={self.quantity})>"
