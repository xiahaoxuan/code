from flask import Blueprint, render_template, request
from basic import Basic
import json

warning = Blueprint('warning', __name__)


@warning.route('/warning/index')
def index():
    return render_template('/warning/index.html')