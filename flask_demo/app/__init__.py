from flask import Flask

from setting import DefaultConfig
from app.user.view import user_bp
from ext import db


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DefaultConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)
    return app
