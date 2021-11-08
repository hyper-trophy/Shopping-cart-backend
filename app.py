from flask import Flask, request

from database.services import add_to_cart

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello, World!'

@app.route('/')
def barcode():
    try:
        product_id = request.args.get('barcode')
        print("id: "+str(product_id))
        add_to_cart(product_id)
        return 'OK'
    except:
        return 'transaction unsuccessful'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
  