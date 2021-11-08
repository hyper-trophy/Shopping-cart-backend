from flask import Flask, request

from database.services import *

app = Flask(__name__)

@app.route('/bill')
def index():
    return get_bill()

@app.route('/')
def barcode():
    try:
        product_id = request.args.get('barcode')
        print("id: "+str(product_id))
        add_to_cart(product_id)
        return 'OK'
    except:
        return 'transaction unsuccessful'

@app.route('/total')
def total():
    return get_total();
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
  