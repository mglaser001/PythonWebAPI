from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.service.userService import userEndpoint
from api.service.authService import auth
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    db.init_app(app)

    app.register_blueprint(userEndpoint, url_prefix = '/user')
    app.register_blueprint(auth, url_prefix = '/auth')

    import userModel

    create_database(app)

    return app

def create_database(app):
    if not path.exists('MGlaserAPIWebApp/' + DB_NAME):
        db.create_all(app=app)
        print('+++ DATABASE CREATED +++')

app = create_app()

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True, port=8001)