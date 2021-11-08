from database.base import Session
from database.Schemas.cart import *


def insert_cart(product_id, quantity, amount):
    try:
        db_session = Session()
        item = Cart(product_id, quantity, amount)
        db_session.add(item)
        db_session.commit()
    except:
        print("⛔ Cannot insert into Cart")
    finally:
        db_session.close()

def update_cart(item, new_quantity, new_amount):
    try:
        db_session = Session()
        item.quantity = new_quantity
        item.amount = new_amount
        db_session.commit()
    except:
        print("⛔ Cannot update Cart")
    finally:
        db_session.close()

def get_record_cart(product_id):
    try:
        db_session = Session()
        item = Cart.query.filter(Cart.product_id == product_id).first()
        db_session.close()
        return item
    except:
        print("⛔ Cannot read Cart")
        db_session.close()
