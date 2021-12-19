from flask import Blueprint, render_template, request
from basic import Basic
import json

notification = Blueprint('notification', __name__)


@notification.route('/notification/index')
def index():
    return render_template('/notification/index.html')
