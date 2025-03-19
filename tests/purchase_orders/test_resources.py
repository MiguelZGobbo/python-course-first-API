import json

def test_get_purchase_orders(test_client):
    response = test_client.get('/purchase_orders')

    assert response.status_code == 200
    assert response.json[0]['id'] == 1

def test_post_purchase_orders(test_client):
    obj = {'id': 2}
    response = test_client.post(
        data = json.dumps(obj),
        contente_type = 'application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == obj['id']