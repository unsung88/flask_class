#from database import Database
from sa import sa

class ItemModel(sa.Model):

    __tablename__ = 'items'
    id = sa.Column(sa.Integer, primary_key = True)
    name = sa.Column(sa.String(90))
    price = sa.Column(sa.Float(precision=2))
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.id'))
    store = sa.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()
        #mode = 'single'
        #db = Database()
        #sql = 'SELECT * from items WHERE name=?'
        #db.execute(mode, sql, (name,))
        #row = db.res.fetchone()
        #db.close()
        #if row:
        #    return cls(*row)


    def save_to_db(self):
        sa.session.add(self)
        sa.session.commit()
        # mode = 'single'
        # db = Database()
        # sql = 'INSERT INTO items VALUES(?,?)'
        # db.execute(mode, sql, (self.name, self.price))
        # db.conn.commit()                
        # db.close()


    def delete_from_db(self):
        sa.session.delete(self)
        sa.session.commit()

    # def update_item(self):

        # mode = 'single'
        # db = Database()
        # sql = 'UPDATE items SET price=? WHERE name=?'
        # db.execute(mode, sql, (self.name, self.price))
        # db.conn.commit()                
        # db.close()