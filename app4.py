from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.userRegister import UserRegister
from resources.store import Store, StoreList
from resources.item import Item, ItemList

app4 = Flask(__name__)
app4.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app4.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app4.secret_key = 'emir'
api = Api(app4)


@app4.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app4, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app4)
    app4.run(port=4997, debug=True)
