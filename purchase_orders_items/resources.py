"""Endpoints REST para itens de pedidos de compra.

Fornece rotas para consultar e criar itens de pedidos de compra.
Aplica autenticação via JWT e delega regras de negócio à camada de serviço.
"""

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from .services import PurchaseOrdersItemsServices

class PurchaseOrdersItems(Resource):
    """Resource para operações sobre itens de um pedido de compra."""

    __service__ = PurchaseOrdersItemsServices()

    # Define e valida parâmetros de entrada para criação de item
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type = str,
        required = True,
        help = 'Informe uma descrição válida!'
    )

    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'Informe um preço válido!'
    )

    parser.add_argument(
        'quantity',
        type = int,
        required = True,
        help = 'Informe uma quantidade válida!'
    )

    @jwt_required()
    def get(self, id):
        """Retorna todos os itens de um pedido (requer autenticação)."""
        return self.__service__.find_by_purchase_order_id(id)
    
    @jwt_required()
    def post(self, id):
        """
        Cria um novo item para o pedido informado (requer autenticação).

        O ID do pedido é passado na rota e incluído automaticamente nos dados
        enviados para a camada de serviço.
        """
        
        data = PurchaseOrdersItems.parser.parse_args()
        data['purchase_order_id'] = id
        return self.__service__.create(**data)
