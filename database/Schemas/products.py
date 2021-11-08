from database.base import Base
from sqlalchemy import Column, String, Integer, Date

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price