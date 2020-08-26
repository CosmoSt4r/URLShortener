from app import db
from datetime import datetime


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.String(2040))
    short = db.Column(db.String(100), unique=True)
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, long, short):
        self.long = long
        self.short = short

    def __repr__(self):
        return f'<URL {self.id}:{self.short}>'

