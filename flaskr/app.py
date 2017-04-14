# all the imports
from flask import Flask
from flask_login import LoginManager

from flaskr.model import db, User


def create_app():
    app = Flask('flaskr')
    app.config.from_object('.config')
    init_login(app)
    register_database(app)
    return app


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()

def register_database(app):
    db.init_app(app)
