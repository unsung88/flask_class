#! /usr/bin/env python3

from flask import Flask 
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
#from db_utils import Utils
from resources.item import Items, Item
from resources.store import Stores, Store

#Create app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'w00t'
#Cretae API
api = Api(app)


@app.before_first_request
def create_tables():
	sa.create_all()



jwt = JWT(app, authenticate, identity)

#Utils.create_user_table()
#Utils.create_items_table()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
	
	from sa import sa
	sa.init_app(app)

	app.run(port=6565, debug=True)
