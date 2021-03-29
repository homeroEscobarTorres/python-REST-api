from flask import Flask
from flask_restful import Api
from db import db

from resources.product import Product, ProductList
from resources.order import Order, OrderByUser, OrderList
from resources.user import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) #Api permette di aggiungere delle risorse

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Product, '/products/<int:productId>')
api.add_resource(ProductList, '/products')
api.add_resource(Order, '/orders/<int:orderId>')
api.add_resource(OrderByUser, '/orders/user/<int:userId>')
api.add_resource(OrderList, '/orders')
api.add_resource(User, '/users/<int:userId>')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)