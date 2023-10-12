from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    text = db.Column(db.String(1000))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(), default=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))

def init_db():
    db.create_all()

    # Create a test user
    new_user = User('a@a.com', 'aaaaaaaa')
    db.session.add(new_user)
    db.session.commit()

    db.session.commit()


if __name__ == '__main__':
    init_db()