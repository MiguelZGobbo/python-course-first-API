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

class PurchaseOrdersItems(Resource):
     
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': 'Pedido de id:{} não encontrado!'.format(id)})