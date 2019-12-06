from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.userRegister import UserRegister
from resources.store import Store, StoreList
from resources.item import Item, ItemList

app4 = Flask(__name__)
app4.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app4.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app4.secret_key = 'emir'
api = Api(app4)


jwt = JWT(app4, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app4.run(port=4997, debug=True)
