from flask import Flask

from setting import DevelopmentConfig
from ext import api, db
from apps.user.view import user_bp


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    api.init_app(app)
    db.init_app(app)
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
