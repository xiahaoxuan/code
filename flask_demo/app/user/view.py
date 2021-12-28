from flask import Blueprint, render_template, make_response, request

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def main():
    # dict_user = {
    #     'username': '备案学习界面'
    # }
    # result_all = User.query.all()
    # result = result_all[0]
    # print(result.username)
    # username = '张三'
    # password = '456789'
    # dict_user = {'username':username, 'password': password}
    # user = User(**dict_user)
    # db.session.add(user)
    # db.session.commit()
    # response = render_template('main/index.html', user=dict_user)
    return 'hello world123'


@user_bp.route('/index')
def index():
    dict_user = {
        'username': '备案学习界面2'
    }
    html = render_template('user/index.html', user=dict_user)
    return make_response(html, 200)


@user_bp.route('/register', methods=["GET", "POST"], endpoint='register')
def register():
    if request.method == "GET":
        return render_template('user/rergister.html')
    else:
        # print(request.args.get('username'))
        # print(request.args.get('address'))
        print(request.form.get('username'))
        print(request.form.get('address'))
        return '注册提交'
