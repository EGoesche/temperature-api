from app import db

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    degrees = db.Column(db.Float)