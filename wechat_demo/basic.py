
import config
import requests
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %
                   (config.APPID, config.APPSECRET))
        urlResp = json.loads(requests.get(url=postUrl).text)
        print(urlResp)
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
        print(self.__accessToken)

    # 外部获取 access_token 接口，同样 leftTime 如果小于十秒我们就刷新 access_token
    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    # 外部获取 openid 接口，同样 leftTime 如果小于十秒我们就刷新 access_token
    def getOpenID(self, code):
        # 通过code获取用户openid
        if not code:  # 缺少code参数
            return 0
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' \
              % (config.APPID, config.APPSECRET, code)
        response = requests.get(url)
        json_str = response.text
        resp_dict = json.loads(json_str)
        if "errcode" in resp_dict:  # 获取access_token失败
            return 0
        open_id = resp_dict.get('openid')
        return open_id

    # 刷新 leftTime，如果小于十秒我们就刷新 access_token
    def run(self):
        while True:
            if self.__leftTime > 10:
                pass
                # time.sleep(2)
                # self.__leftTime -= 2
            else:
                self.__real_get_access_token()
