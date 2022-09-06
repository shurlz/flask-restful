from application import db
from application import app

class schedule(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.String(), nullable=False, unique=True)
    date = db.Column(db.String(), nullable=False)
    time = db.Column(db.String(), default='00:00:00')
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return task
