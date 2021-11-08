from sqlalchemy.sql.schema import ForeignKey
from database.base import Base
from sqlalchemy import Column, String, Integer, Date
from database.Schemas.products import *

class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    amount = Column(Integer)

    def __init__(self, product_id, quantity, amount):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
