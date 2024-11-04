"""
File Description: This file is the main file of the api package. It is responsible for creating the Flask app and the database. It also registers the blueprints for the auth routes.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'please dont steal my key it is secret'

    # for database initialization
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # for jwt (json web token ) token 
    app.config['JWT_SECRET_KEY'] = 'please dont steal or else I will be :( '  # Change this to a strong key
    jwt = JWTManager(app)

    #from .views import views
    from .auth import auth

    #app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import models database
    from .models import User
    
    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('api/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')