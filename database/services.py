from database.Operations.cart import *

#CAUTION: HARDCODING
def add_to_cart(product_id):
    # try:
        item = get_record_cart(product_id)
        if item==None:
            insert_cart(product_id, 1, 100)
        else:
            update_cart(product_id, item.quantity+1, 200)
    # except:
    #     print("⛔ error in adding to cart")