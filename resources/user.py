#from database import Database
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="username is required")
    parser.add_argument('password', type=str, required=True, help="password is required")

    def post(self):
        post_data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(post_data['username']):
            return {"error": "Username is already in use"}, 400
        user = UserModel(**post_data) #post_data['username'], post_data['password'])
        user.save_to_db()

        # db = Database()
        # mode = 'single'
        # sql = 'INSERT INTO users VALUES (NULL, ?,?)'
        # db.execute(mode, sql, (post_data['username'], post_data['password']) )
        # db.conn.commit()
        # db.close()
        return {"message" : "User created successfully"}, 201

