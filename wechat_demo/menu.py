import json
import requests
from urllib import parse
import config


class Menu(object):
    # 绑定用户
    bind_url_encode = parse.quote('http://test.wechat.rzyckz.com/user/bind')
    bind_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s' \
               '&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (config.APPID, bind_url_encode)
    rebind_url_encode = parse.quote('http://test.wechat.rzyckz.com/user/rebind')
    # 换绑用户
    rebind_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s' \
                 '&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (config.APPID, rebind_url_encode)
    # 解除绑定
    unbind_url_encode = parse.quote('http://test.wechat.rzyckz.com/user/unbind')
    unbind_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s' \
                 '&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (config.APPID, unbind_url_encode)
    # 推送管理
    notification_url_encode = parse.quote('http://test.wechat.rzyckz.com/notification/index')
    notification_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s' \
                       '&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (
                           config.APPID, notification_url_encode)
    # 解除绑定
    waring_url_encode = parse.quote('http://test.wechat.rzyckz.com/waring/index')
    waring_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s' \
                 '&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (config.APPID, waring_url_encode)
    postData = {
        "button": [{
            "name": "账号管理",
            "sub_button": [{
                "type": "view",
                "name": "绑定账号",
                "url": bind_url
            },
                {
                    "type": "view",
                    "name": "换绑账号",
                    "url": rebind_url
                }, {
                    "type": "view",
                    "name": "解绑账号",
                    "url": unbind_url
                }
            ]
        },
            {
                "type": "view",
                "name": "推送管理",
                "url": notification_url
            },
            {
                "type": "view",
                "name": "预警管理",
                "url": waring_url
            }
        ]
    }

    postJson = json.dumps(postData, ensure_ascii=False)

    def create(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        req = requests.post(postUrl, self.postJson.encode('utf-8'))
        print(req.text)

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        req = requests.get(postUrl)
        print(req.text)

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        req = requests.get(postUrl)
        print(req.text)

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        req = requests.get(postUrl)
        print(req.text)
