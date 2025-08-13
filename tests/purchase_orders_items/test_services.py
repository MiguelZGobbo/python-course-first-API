"""Testes para os serviços de itens de pedidos de compra."""

import pytest
from purchase_orders_items.services import PurchaseOrdersItemsServices
from exceptions.exceptions import QuantityException

def test_check_maximum_po_quantity(seed_db, test_client):
     """
    Testa a validação de quantidade máxima de itens em um pedido de compra.

    Verifica se o método _check_maximum_purchase_order_quantity da classe
    PurchaseOrdersItemsServices levanta a exceção QuantityException com código 400
    e mensagem apropriada quando a quantidade excede o limite do pedido.
    """
     with test_client.application.app_context():
        with pytest.raises(QuantityException) as ex:
            PurchaseOrdersItemsServices()._check_maximum_purchase_order_quantity(seed_db['purchase_order'].id, seed_db['purchase_order'].quantity, 30)
        assert ex.value.code == 400
        assert ex.value.description == 'Você só pode adicionar mais 20 itens'