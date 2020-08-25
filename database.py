from app import db
from datetime import datetime


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old = db.Column(db.String(2040))
    new = db.Column(db.String(16), unique=True)
    hits = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Url, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<URL {self.old}>'

