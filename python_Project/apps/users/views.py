from flask import Blueprint
from apps.users.models import User
from exts.redis_util import Redis

user_bp = Blueprint("user", __name__)


@user_bp.route('/')
def main():
    # user = User.query.all()
    # print(user)
    Redis.write("test_key", "test_value", 60)
    return '你好'
