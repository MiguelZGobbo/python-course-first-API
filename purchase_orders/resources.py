from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido 1',
        'items': [
            {
                'id': 1,
                'description': 'Laranja',
                'price': 5.75
            }
        ]
    }
]

class PurchaseOrders(Resource):

    def get(self):
        return jsonify(purchase_orders)