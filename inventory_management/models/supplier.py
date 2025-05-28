from sqlalchemy import Column, Integer, String
from models import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)

    def __repr__(self):
        return f"<Supplier(name={self.name})>"
