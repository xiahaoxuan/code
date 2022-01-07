import json

from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, jsonify, g
from sqlalchemy import or_

from apps.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from ext import db
from ext.smssend import SmsSendAPIDemo

user_bp = Blueprint('user', __name__)

required_login_list = ['/user/center', '/user/change']


# ****重点*****
@user_bp.before_app_request
def before_request1():
    # print('before_request', request.path)
    if request.path in required_login_list:
        id = session.get('uid')
        if not id:
            return redirect(url_for('user.login'))
        else:
            user = User.query.get(id)
            # g对象，本次请求的对象
            g.user = user

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
            requestId = session.get(phone)
            # 验证code
            params = {
                "requestId": requestId,
                "code": code,
            }
            api = common_api()
            ret = api.check(params)
            print(ret)
            # 查询数据库
            user = User.query.filter(User.phone == phone).first()
            print(user)
            if user:
                # 登录成功
                session['uid'] = user.id
                return redirect(url_for('user.main'))
            else:
                return render_template('user/login.html', msg='此号码未注册')
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
        params = {
            "mobile": phone,
            "templateId": "13484",
            "paramType": "json",
            "params": json.dumps({"code":123})
        }
        api = common_api()
        ret = api.send(params)
        print(ret)
        session[phone] = '189075'
        return jsonify(code=200, msg='短信发送成功！')
    else:
        return jsonify(code=400, msg='没有此用户信息')

# 公共方法
def common_api():
    secret_Id = current_app.config["WANGYI_SECRET_ID"]
    secret_Key = current_app.config["WANGYI_SECRET_KEY"]
    business_Id = current_app.config["WANGYI_BUSINESSID"]
    api = SmsSendAPIDemo(secret_Id, secret_Key, business_Id)
    return api


# 验证手机号码
@user_bp.route('/check/phone')
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).first()
    # code: 400 不能用    200 可以用
    if user:
        return jsonify(code=400, msg='此号码已被注册')
    else:
        return jsonify(code=200, msg='此号码可用')


# 修改用户信息
@user_bp.route('/user/change', methods=["GET", "POST"])
def user_change():
    if request.method == "POST":
        username = request.form.get('username')
        phone = request.form.get('phone')
        email = request.form.get('email')
        icon = request.files.get('icon')
        user = g.user
        user.username = username
        user.phone = phone
        user.email = email
        db.session.commit()
    return render_template('user/center.html', user=g.user)


# 用户中心
@user_bp.route('/user/center')
def user_center():
    return render_template('user/center.html', user=g.user)
