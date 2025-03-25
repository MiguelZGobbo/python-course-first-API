from db import db

class PurchaseOrdermodel(db.Model):
    __tablename__ = 'purchase_orders'

    id  = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String, nullable = False)

    def __init__(self, description):
        self.description = description