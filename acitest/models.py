import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Contacts(db.Model):
    __tablename__ = 'Contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    #password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    date_signed_up = db.Column(db.DateTime)
