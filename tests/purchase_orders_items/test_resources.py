import json

def test_get_items_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/1/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1

def test_get_items_purchase_order_id_not_found(test_client):
    id = 999
    response = test_client.get('/purchase_orders/{}/items'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Pedido de id:{} não encontrado!'.format(id)

def test_post_purchase_order_item(test_client):
    obj = {'id': 2, 'description': '', 'price': int }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data = json.dumps(obj),
        constext_type = 'application//json'
    )
     
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert len(response.json['items']) == 2
    assert response.json['items'][1]['id'] == obj('id')