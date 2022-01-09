from flask import Blueprint

article_bp = Blueprint('article', __name__)


@article_bp.route('/article/publish', methods=["GET", "POST"])
def publish_article():
    return "发布"
