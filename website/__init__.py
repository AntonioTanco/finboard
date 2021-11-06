from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "datebase.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "chicken"
    app.config['SQLAlchemy_DATEBASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import User, Note

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

def create_datebase(app):
    if not path('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created Datebase!")