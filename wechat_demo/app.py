from flask import Flask, request, abort, render_template
import hashlib
import xmltodict
import time
import config
from menu import Menu
import accessToken
from gevent import pywsgi
import urllib
import json


app = Flask(__name__)


@app.route('/wechat', methods=["POST", "GET"])
def wechat():  # put application's code here
    # 对接微信公众号服务器
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    # 校验参数
    if not all([signature, timestamp, nonce]):
        abort(400)
    tmp = [config.WECHAT_TOKEN, timestamp, nonce]
    tmp.sort()
    tmp = "".join(tmp)
    tmp = hashlib.sha1(tmp.encode()).hexdigest()
    if tmp == signature:
        # 表示是微信发送的请求
        if request.method == 'GET':   # 验证token
            print('第一次接入微信服务器的验证')
            if not echostr:
                abort(400)
            return echostr
        elif request.method == 'POST':  # 其他消息类型
            print('接收到其他消息认证')
            # xml_str = wechat_post()
            return ''

    else:
        abort(403)


def wechat_post():
    xml_str = request.data
    if not xml_str:
        abort(400)
    xml_dict = xmltodict.parse(xml_str)
    xml_dict = xml_dict.get('xml')
    msg_type = xml_dict.get('MsgType')
    # 表示发送的是文本消息
    # 构造返回值，回复给微信服务器回复用户的消息内
    if msg_type == 'text':
        resp_dict = {
            "xml": {
                "ToUserName": xml_dict.get('FromUserName'),
                "FromUserName": xml_dict.get('ToUserName'),
                "CreateTime": int(time.time()),
                "MsgType": xml_dict.get('MsgType'),
                "Content": xml_dict.get('Content'),
                "MsgId": xml_dict.get('resp_dict'),
            }
        }
        print(resp_dict)
        xml_str = xmltodict.unparse(resp_dict)
        return xml_str
    elif msg_type == 'event':
        msg_event = xml_dict.get('Event')
        if msg_event == 'CLICK':
            content = "编写中，尚未完成"
            resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get('FromUserName'),
                    "FromUserName": xml_dict.get('ToUserName'),
                    "CreateTime": int(time.time()),
                    "MsgType": 'text',
                    "Content": content,
                    "MsgId": xml_dict.get('resp_dict'),
                }
            }
            print(resp_dict)
            xml_str = xmltodict.unparse(resp_dict)
            return xml_str
        else:
            return ''

    else:
        return ""


@app.route("/wechat/index")
def index():
    """
    让用户通过微信访问的网页视图
    :return:
    """
    code = request.args.get('code')
    if not code:
        return u'缺少code参数'
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' \
          % (config.APPID, config.APPSECRET, code)
    response = urllib.request.urlopen(url)
    json_str = response.read()
    resp_dict = json.loads(json_str)
    print('第一个数据%s' % resp_dict)
    if "errcode" in resp_dict:
        return u'获取access_token失败'
    access_token = resp_dict.get('access_token')
    open_id = resp_dict.get('open_id')
    # 向微信服务器发送http请求
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' \
          % (access_token, open_id)
    response = urllib.request.urlopen(url)
    json_str = response.read()
    resp_dict = json.loads(json_str)
    print('第二个数据%s' % resp_dict)
    if "errcode" in resp_dict:
        return u'获取access_token失败'
    return render_template('index.html')


def register_blueprints():
    from controller.account import account
    from controller.notification import notification
    from controller.warning import warning
    app.register_blueprint(account)
    app.register_blueprint(notification)
    app.register_blueprint(warning)

if __name__ == '__main__':
    # 设置菜单，其实只运行一次就行
    menu = Menu()
    access_token = accessToken.getAccessToken()
    menu.create(access_token)
    # 注册蓝图
    register_blueprints()
    # 启动wsgi服务
    server = pywsgi.WSGIServer(('0.0.0.0', 80), app)
    server.serve_forever()

    # app.run(port=80, host='0.0.0.0', debug=True)
