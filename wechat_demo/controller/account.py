from flask import Blueprint, render_template, request
from basic import Basic
import json

account = Blueprint('account', __name__)


@account.route('/user/bind')
def bind_account():
    # code = request.args.get('code', 0)
    # open_id = Basic().getOpenID(code)
    # if open_id:
    #     return render_template('/account/index.html', open_id=open_id)
    # return '无法获取用户id'
    open_id = ''
    return render_template('/account/index.html', open_id=open_id)


@account.route('/user/check', methods=['GET', 'POST'])
def check_account():
    try:
        data = json.loads(request.data)
        print(data)
        username = data.get('username')
        password = data.get('password')
        return '1234567'
    except:
        return 0


@account.route('/user/rebind')
def rebind_account():
    code = request.args.get('code', 0)
    open_id = Basic().getOpenID(code)
    if open_id:
        return render_template('/account/rebind.html', open_id=open_id)
    return '无法获取用户id'
    # open_id = ''
    # return render_template('/account/rebind.html', open_id=open_id)

@account.route('/user/unbind')
def unbind_account():
    try:
        code = request.args.get('code', 0)
    except:
        code = 0
    # open_id = Basic().getOpenID(code)
    # if open_id:
    #     return render_template('/account/index.html', open_id=open_id)
    # return '无法获取用户id'
    # open_id = ''
    return render_template('/account/index.html', flag=1)









