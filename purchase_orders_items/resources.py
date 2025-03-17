from flask_restful import Resource
from flask import jsonify

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

class PurchaseOrdersItems(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po["items"])
        return ("Id não encontrado!")