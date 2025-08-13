"""Camada de serviço para itens de pedidos de compra.

Contém regras de negócio e validações antes de persistir ou recuperar
dados da camada de modelo.
"""

from purchase_orders.model import PurchaseOrderModel
from .model import PurchaseOrdersItemsModel
from flask import jsonify
from exceptions.exceptions import QuantityException

class PurchaseOrdersItemsServices():
    """Fornece operações de negócio para itens de pedidos de compra."""

    def _check_maximum_purchase_order_quantity(self, purchase_order_id, purchase_order_quantity, quantity):
        """
        Valida se a adição de novos itens não ultrapassa o limite do pedido.

        A regra de negócio define que a soma das quantidades de todos os itens
        não pode exceder a quantidade total estipulada no pedido de compra.
        """

        purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(
            purchase_order_id)

        sum_items = 0
        for poi in purchase_orders_items:
            sum_items += poi.quantity

        if sum_items + quantity > purchase_order_quantity:
            raise QuantityException('Você só pode adicionar mais {} itens'.format(
                purchase_order_quantity - sum_items))

    def find_by_purchase_order_id(self, purchase_order_id):
        """
        Retorna todos os itens vinculados a um pedido.

        Caso o pedido não exista, retorna mensagem informativa.
        """

        purchase_order = PurchaseOrderModel.find_by_id(purchase_order_id)

        if purchase_order:
            purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(purchase_order_id)
            
            return [p.as_dict() for p in purchase_orders_items]
        return jsonify({'message': 'Pedido de id:{} não encontrado!'.format(purchase_order_id)})
    
    def create(self, **kwargs):
        """
        Cria e salva um novo item para um pedido de compra existente.

        Antes de salvar, valida se a quantidade não ultrapassa o limite
        definido no pedido.
        """
        
        purchase_order = PurchaseOrderModel.find_by_id(kwargs['purchase_order_id'])
        if purchase_order:
            self._check_maximum_purchase_order_quantity(
                kwargs['purchase_order_id'],
                purchase_order.quantity,
                kwargs['quantity']
            )
            purchase_orders_item = PurchaseOrdersItemsModel(**kwargs)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()
        
        return jsonify({'message':'Pedido de id:{} não encontrado'.format(kwargs['purchase_order_id'])})