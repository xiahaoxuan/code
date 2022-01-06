from flask import Blueprint, render_template, make_response, request, session, redirect, url_for, jsonify
from sqlalchemy import or_

from apps.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from ext import db

user_bp = Blueprint('user', __name__)


# 首页
@user_bp.route('/')
def main():
    uid = session.get('uid')
    if uid:  # 说明已经登录
        user = User.query.get(uid)
        return render_template('user/index.html', user=user)
    else:
        return render_template('user/index.html')


# 注册
@user_bp.route('/register', methods=["GET", "POST"], endpoint='register')
def register():
    if request.method == "GET":
        return render_template('user/register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == repassword and username and phone:
            user_name = User.query.filter_by(username=username).first()
            if user_name:
                return render_template('user/register.html', msg="用户名已被注册")
            user_phone = User.query.filter_by(phone=phone).first()
            if user_phone:
                return render_template('user/register.html', msg="手机号码已被注册")
            else:
                user = User()
                user.username = username
                user.password = generate_password_hash(password)
                user.phone = phone
                user.email = email
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('user.main'))
        return render_template('user/register.html')


# 登录
@user_bp.route('/login', methods=["GET", "POST"], endpoint='login')
def login():
    if request.method == "POST":
        f = request.args.get('f')
        if f == '1':  # 用户名跟密码登录
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter(or_(User.username == username, User.phone == username)).first()
            if user:
                flag = check_password_hash(user.password, password)
                if flag:
                    session["uid"] = user.id
                    return redirect(url_for('user.main'))
                else:
                    return render_template('user/login.html', msg='用户名或密码错误')
            else:
                return render_template('user/login.html', msg='用户名或密码错误')
        elif f == '2':  # 手机号码登录
            phone = request.form.get('phone')
            code = request.form.get('code')

            # user = User.query.filter_by(phone=)
    else:
        return render_template('user/login.html')


# 退出
@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.main'))


# 发送验证码
@user_bp.route('/user/sendMsg', methods=["GET", "POST"])
def send_message():
    phone = request.args.get('phone')
    user = User.query.filter_by(phone=phone).first()
    if user:
        return jsonify(code=200, msg='没有此用户信息')
    else:
        return jsonify(code=400, msg='没有此用户信息')


# 验证手机号码
@user_bp.route('/check/phone')
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).first()
    # code: 400 不能用    200 可以用
    if user > 0:
        return jsonify(code=400, msg='此号码已被注册')
    else:
        return jsonify(code=200, msg='此号码可用')


# 修改用户信息
@user_bp.route('/user/change')
def user_change():
    return '修改用户'


# 用户中心
@user_bp.route('/user/center')
def user_center():
    return render_template('user/center.html')
