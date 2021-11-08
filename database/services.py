from database.Operations.cart import *
from database.Operations.products import *
from sqlalchemy import Table , MetaData
from database.base import engine
from prettytable import PrettyTable

def get_bill():
    metadata = MetaData(engine)

    v = Table('bill', metadata, autoload=True)
    t = PrettyTable(['Product', 'Quantity', 'Amount'])

    tot_amt = 0
    tot_qty = 0
    for r in engine.execute(v.select()):
        tot_amt+=r[2]
        tot_qty+=r[1]
        t.add_row([r[0], r[1], r[2]])
    t.add_row(['Total', tot_qty, tot_amt])
    return t.get_html_string().replace('<table>', '<style>table, th, td {border: 1px solid black;border-collapse: collapse; padding: 0.5rem}</style><table>')

def get_total():
    metadata = MetaData(engine)
    v = Table('bill', metadata, autoload=True)
    tot_amt = 0
    tot_qty = 0
    for r in engine.execute(v.select()):
        tot_amt+=r[2]
        tot_qty+=r[1]
    return str(tot_amt) + '|' + str(tot_qty)

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