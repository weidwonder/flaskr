# all the imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from flaskr.auth.model import db, User
from flaskr.auth.views import auth
from flaskr.views import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskr.config')
    init_login(app)
    register_database(app)
    set_bootstrap(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = u"正在跳转登陆"

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()


def register_database(app):
    db.init_app(app)


def set_bootstrap(app):
    Bootstrap(app)
