from flask import jsonify
from flask_restful import Resource

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

class PurchaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)

