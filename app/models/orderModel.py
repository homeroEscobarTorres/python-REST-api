from db import db
from datetime import datetime

class OrderModel(db.Model):
    __tablename__ = 'orders'

    orderId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    totalPrice = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer)
    creationDate = db.Column(db.String(80))
    
    products = db.relationship('ProductModel', lazy='dynamic') #dynamic evita di creare un oggetto per ogni product nella tabella products, in più ogni volta che verrà richiamato il metodo .json andrà a guardare nella tabella products

    def __init__(self, orderId, userId, totalPrice, quantity, creationDate=str(datetime.now())):
        self.orderId = orderId
        self.userId = userId
        self.totalPrice = totalPrice
        self.quantity = quantity
        self.creationDate = creationDate

    def json(self):
        return {
            'userId': self.userId, 
            'totalPrice': self.totalPrice, 
            'quantity': self.quantity,
            'products': [product.json() for product in self.products.all()] #self.products is a query builder che guarda dentro la tabella products e con .all li recupera tutti 
        }

    @classmethod
    def find_by_order_id(cls, orderId):
        return cls.query.filter_by(orderId=orderId).first()
    
    @classmethod
    def find_by_user_id(cls, userId):
        return cls.query.filter_by(userId=userId).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
