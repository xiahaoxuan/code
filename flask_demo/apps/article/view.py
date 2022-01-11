from flask import Blueprint, request, g, redirect, url_for
from apps.article.models import *

article_bp = Blueprint('article', __name__)


@article_bp.route('/article/publish', methods=["GET", "POST"])
def publish_article():
    if request.method == "POST":
        title = request.form.get('title')
        type_id = int(request.form.get('type'))
        content = request.form.get('content')
        article = Article()
        article.title = title
        article.type_id = type_id
        article.content = content.encode('utf-8')
        article.user_id = g.user.id
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('user.main'))

