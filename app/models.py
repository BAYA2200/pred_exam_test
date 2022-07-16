from app import db


class Customer(db.Model):
    id = db.Column(db.Integer(primary_key=True))
    name = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    item = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeyignKey("position.id"))
    user = db.relationship("User", backref=db.backref())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)