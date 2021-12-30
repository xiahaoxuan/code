from flask import Flask
from setting import DefaultConfig
from apps.users.views import user_bp
from exts import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)
    return app
