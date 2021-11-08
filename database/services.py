from database.Operations.cart import *
from database.Operations.products import *

#CAUTION: HARDCODING
def add_to_cart(product_id):
    try:
        item = get_record_cart(product_id)
        product = get_record_products(product_id)
        if item==None:
            insert_cart(product_id, 1, product.price)
        else:
            new_quantity = item.quantity + 1
            new_amount = product.price*new_quantity
            update_cart(product_id, new_quantity, new_amount)
    except:
        print("⛔ error in adding to cart")