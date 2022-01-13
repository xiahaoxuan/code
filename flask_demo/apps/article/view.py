from flask import Blueprint, request, g, redirect, url_for, render_template, jsonify
from apps.article.models import *
from apps.user.models import Photo
from ext.qiniu_storage import upload_qiniu

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


@article_bp.route('/article/detail')
def article_detail():
    detail_id = request.args.get('aid')
    article = Article.query.get(detail_id)
    # 获取文章分类
    types = Article_type.query.all()
    return render_template('article/detail.html', article=article, types=types, user=g.user)


@article_bp.route('/love')
def article_love():
    article_id = request.args.get('aid')
    tag = request.args.get('tag')

    article = Article.query.get(article_id)
    if tag == '1':
        article.love_num -= 1
    else:
        article.love_num += 1
    db.session.commit()
    return jsonify(num=article.love_num)


@article_bp.route('/photo/upload', methods=["GET", "POST"])
def upload_photo():
    photo_file = request.files.get('photo')
    ret, info = upload_qiniu(photo_file)
    if info.status_code == 200:
        photo = Photo()
        photo.photo_name = ret['key']
        photo.user_id = g.user.id
        db.session.add(photo)
        db.session.commit()
        return '上传成功！'
    else:
        return '上传失败！'