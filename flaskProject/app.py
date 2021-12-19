from flask import Flask, request, abort, render_template
import hashlib

import xmltodict
from gevent import pywsgi

import time
import urllib.request
import json


APPID = 'wx3fbd00d000d911a1'
APPSECRET = 'df11f7a6397bb823f261e2732cb12e06'
WECHAT_TOKEN = 'xiahaoxuan2021'

app = Flask(__name__)


@app.route('/wechat', methods=["POST", "GET"])
def wechat():  # put application's code here
    # 对接微信公众号服务器
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    # echostr = request.args.get("echostr")
    # 校验参数
    if not all([signature, timestamp, nonce]):
        abort(400)
    tmp = [WECHAT_TOKEN, timestamp, nonce]
    tmp.sort()
    tmp = "".join(tmp)
    tmp = hashlib.sha1(tmp.encode()).hexdigest()
    if tmp == signature:
        # 表示是微信发送的请求
        if request.method == 'GET':
            print('第一次接入微信服务器的验证')
            echostr = request.args.get("echostr")
            if not echostr:
                abort(400)
            return echostr
        elif request.method == 'POST':
            # return ''
            xml_str = request.data
            if not xml_str:
                abort(400)
            xml_dict = xmltodict.parse(xml_str)
            xml_dict = xml_dict.get('xml')
            msg_type = xml_dict.get('MsgType')
            # 表示发送的是文本消息
            # 构造返回值，回复给微信服务器回复用户的消息内
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
            xml_str = xmltodict.unparse(resp_dict)
            return xml_str

    else:
        abort(403)


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
          % (APPID, APPSECRET, code)
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
    return render_template('index.html', user=resp_dict)


if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0', 80), app)
    # server.serve_forever()
    app.run(port=80, host='0.0.0.0', debug=True)
