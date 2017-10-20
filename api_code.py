#! /usr/bin/env python3
import os
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
#set the database URI to DATABASE_URL env var if present or sqlite is not
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
#'postgres://ggpsizvybowzud:6252c858561f322786e4433e2ced44fb8bba98f3efbfdd4e15aa8c3fa2f9ded4@ec2-54-235-88-58.compute-1.amazonaws.com:5432/d89qtfk2vl362v' 
#'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'w00t'
#Cretae API
api = Api(app)


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
