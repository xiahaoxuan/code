from flask import Flask

from setting import DefaultConfig
from apps.user.view import user_bp



def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DefaultConfig)
    app.register_blueprint(user_bp)
    return app
