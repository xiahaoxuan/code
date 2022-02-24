from flask import Blueprint
from flask_restful import Resource, marshal_with
from ext import api

from apps.user.models import User

user_bp = Blueprint('user', __name__)


class hello_world(Resource):
    @marshal_with
    def get(self):
        # Default to 200 OK
        user = User.query.all()
        return {'task': 'Hello world'}

    def post(self):
        return {"age": 18}


api.add_resource(hello_world, '/')
