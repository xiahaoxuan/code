import hashlib
import urllib.parse

import xmltodict
# tmp = '1639022904454333606xiahaoxuan2021'
# tmp = hashlib.sha1(tmp.encode())
# tmp = tmp.hexdigest()
# print(tmp)
# xml_str = """
# <xml>
# <ToUserName><![CDATA[gh_866835093fea]]></ToUserName>
# <FromUserName><![CDATA[ogdotwSc_MmEEsJs9-ABZ1QL_4r4]]></FromUserName>
# <CreateTime>1478317060</CreateTime>
# <MsgType><![CDATA[text]]></MsgType>
# <Content><![CDATA[你好]]></Content>
# <MsgId>6349323426230210995</MsgId>
# </xml>
# """
# xml_dict = xmltodict.parse(xml_str)
# print(xml_dict['xml'])
# for key, value in xml_dict["xml"].items():
#     print(key, '=', value)

xml_dict = {
    "xml": {
        "ToUserName": "gh_866835093fea",
        "FromUserName": "ogdotwSc_MmEEsJs9-ABZ1QL_4r4",
        "CreateTime": "1478317060",
        "MsgType": "text",
        "Content": u"你好",
        "MsgId": "6349323426230210995",
    }
}
xml_str = xmltodict.unparse(xml_dict)
url = 'http://101.33.211.216/wechat/index'

print(urllib.parse.quote(url))