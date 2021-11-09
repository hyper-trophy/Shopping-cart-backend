from flask import Flask, request

from database.services import *

app = Flask(__name__)

@app.route('/ping')
def main():
    return 'pong!'

@app.route('/add')
def barcode():
    product_id = request.args.get('barcode')
    if product_id==None:
        return "please add barcode query parameter"
    print("id: "+str(product_id))
    result = add_to_cart(product_id)
    if result==False:
        return 'Transaction unsuccessful, check product id'
    return 'OK'

@app.route('/bill')
def index():
    return get_bill()


@app.route('/total')
def total():
    return get_total()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
  