#from database import Database
from sa import sa

class UserModel(sa.Model):
    #SQLAlchemy setup
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key = True)
    username = sa.Column(sa.String(80))
    password = sa.Column(sa.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_to_db(self):
        sa.session.add(self)
        sa.session.commit()


    def delete_from_db(self):
        sa.session.delete(self)
        sa.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
        # db = Database()
        # mode = 'single'
        # query = 'SELECT * FROM users WHERE username=?'
        # db.execute(mode, query, (username,))
        # row = db.res.fetchone()
        # db.close()
        # user = None
        # if row:
        #     user = cls(*row)
        # return user

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(id = userid).first()
        # db = Database()
        # mode = 'single'
        # query = 'SELECT * FROM users WHERE id=?'
        # db.execute(mode, query, (userid,))
        # row = db.res.fetchone()
        # db.close()
        # user = None
        # if row:
        #     user = cls(*row)
        # return user
