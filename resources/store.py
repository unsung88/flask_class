from flask_restful import Resource, reqparse
#from flask_jwt import JWT, jwt_required
from models.store import StoreModel




class Stores(Resource):

	def get(self):
		stores = [store.json() for store in StoreModel.query.all()]
		allstores = {"stores": stores}
		if stores:
			return allstores, 200
		return {'error': 'No stores found'}, 404


class Store(Resource):
	
	#@jwt_required()
	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json(), 200
		return {'error': 'Store, ' + name + ' not found'}, 404 


	def post(self, name):
		if StoreModel.find_by_name(name):
			return {"Error": "This store already exists"}, 400
		new_store = StoreModel(name)
		try:
			new_store.save_to_db()
		except Exception as e:
			return {'error': 'Create store failed: %s' % e}, 500 
		else:
			return {'store': new_store.json()}, 201


	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()		
			return {'deleted': name}, 200


	# def put(self, name):
	# 	post_data = Store.parser.parse_args()
	# 	store = StoreModel.find_by_name(name)
	# 	if store is None:
	# 		store.save_to_db()
	# 		return {'store': store.json() }, 201
	# 	else:
	# 		store = StoreModel(name, **post_data) #name, post_data['price']) 
	# 		store.save_to_db()
	# 		return {'store': store.json() }, 200