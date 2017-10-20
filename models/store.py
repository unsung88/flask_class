from sa import sa

class StoreModel(sa.Model):

    __tablename__ = 'stores'
    id = sa.Column(sa.Integer, primary_key = True)
    name = sa.Column(sa.String(90))
    #price = sa.Column(sa.Float(precision=2))
    items = sa.relationship('ItemModel', lazy='dynamic')


    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()] } #, 'price': self.price}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()


    def save_to_db(self):
        sa.session.add(self)
        sa.session.commit()


    def delete_from_db(self):
        sa.session.delete(self)
        sa.session.commit()
