# -*- coding: utf-8 -*-
# flake8: noqa
import random

from qiniu import Auth, etag, put_data
from flask import current_app


def upload_qiniu(filestorage):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = current_app.config["QINIU_ACCESS_KEY"]
    secret_key = current_app.config["QINIU_SECRET_KEY"]
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'flask-boke'
    # 上传后保存的文件名
    # 上传后保存的文件名
    filename = filestorage.filename
    ran = random.randint(1, 1000)
    suffix = filename.rsplit('.')[-1]
    key = filename.rsplit('.')[0] + '_' + str(ran) + '.' + suffix
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    localfile = filestorage.read()
    ret, info = put_data(token, key, localfile)
    # print(info)
    return ret, info
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
