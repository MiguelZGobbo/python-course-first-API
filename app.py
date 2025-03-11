from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido compra 1',
        'items': [
            {
                'id': 1,
                'description': 'item pedido 1',
                'price': 29.99
            }
        ]
    }
]

@app.route("/")
def home():
    return "Tamo na net pai! Daqui pra frente é só pra tras :)"

@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id): 
    for po in purchase_orders: 
         if po["id"] == id:
             return jsonify(purchase_orders)
    return ("Id não encontrado")
         
     

app.run(port=5000)

