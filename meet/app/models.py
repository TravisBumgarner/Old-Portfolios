from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    date = db.Column(db.DateTime)
    email = db.Column(db.String(120), index=True, unique=False)
    website = db.Column(db.String(120), index=True, unique=False)
    message = db.Column(db.Text, index=True, unique=False)
