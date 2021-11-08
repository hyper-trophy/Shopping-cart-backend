from database.base import Session
from database.Schemas.products import *

def get_record_products(product_id):
    try:
        db_session = Session()
        item = db_session.query(Products).filter(Products.id == product_id).first()
        db_session.close()
        return item
    except:
        print("⛔ Cannot read Products")
        db_session.close()