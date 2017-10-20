#from database import Database
from flask_restful import Resource, reqparse
#from flask import Flask, request
from flask_jwt import JWT, jwt_required
from models.item import ItemModel




class Items(Resource):

	def get(self):
		items = [item.json() for item in ItemModel.query.all()]
		allitems = {"items": items}
		# mode = 'single'
		# db = Database()
		# sql = 'SELECT * from items'
		# db.execute(mode, sql, ())
		# rows = db.res.fetchall()
		# db.close()
		if items:
			return allitems, 200
		return {'error': 'No items found'}, 404

class Item(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('price', type=float, required=True, help="price is required")
	parser.add_argument('store_id', type=int, required=True, help="store_id is required")

	
	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json(), 200
		return {'error': 'Item, ' + name + ' not found'}, 404 


	def post(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return {"Error": "This item already exists"}, 400
		post_data = Item.parser.parse_args()
		new_item = ItemModel(name, **post_data) #name, post_data['price'] )
		try:
			new_item.save_to_db()
		except Exception as e:
			return {'error': 'Create item failed: %s' % e}, 500 
		else:
			return {'item': new_item.json()}, 201


	def delete(self, name):
		# mode = 'single'
		# db = Database()
		# sql = 'DELETE from items WHERE name=?'
		# db.execute(mode, sql, (name,))
		# db.conn.commit()			 	
		# db.close()
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()		
			return {'deleted': name}, 200


	def put(self, name):
		post_data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		if item is None:
			item.save_to_db()
			return {'item': item.json() }, 201
		else:
			item = ItemModel(name, **post_data) #name, post_data['price']) 
			item.save_to_db()
			return {'item': item.json() }, 200
