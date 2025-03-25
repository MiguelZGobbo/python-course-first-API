from flask import Flask
from flask_restful import Api
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import db

def create_app():

    app = Flask(__name__)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/python_course'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()


    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

    return app


