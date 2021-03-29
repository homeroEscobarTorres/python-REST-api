from db import db
from datetime import datetime


class ProductModel(db.Model):
    __tablename__ = 'products'

    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    creationDate = db.Column(db.String(80))

    orderId = db.Column(db.Integer, db.ForeignKey('orders.orderId'))
    order = db.relationship('OrderModel')

    def __init__(self, productId, name, description, price, orderId, creationDate=str(datetime.now())):
        self.productId = productId
        self.name = name
        self.description = description
        self.price = productId
        self.orderId = orderId
        self.creationDate = creationDate

    def json(self):
        return {
            'productId': self.productId, 
            'name': self.name, 
            'description': self.description, 
            'price': self.price, 
            'creationDate': self.creationDate
        }

    @classmethod
    def find_by_id(cls, productId):
        return cls.query.filter_by(productId=productId).first() #SELECT * FROM products WHERE product_id=productId LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()