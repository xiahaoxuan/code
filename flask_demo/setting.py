import os


class DefaultConfig(object):
    """
    默认配置
    """
    # production development testing
    # 环境配置
    ENV = 'development'
    DEBUG = True

    # 数据库配置
    HOST = '101.33.211.216'
    PORT = '3306'
    DATABASE = 'xhx_study'
    USERNAME = 'root'
    PASSWORD = '940628'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD,
                                                                               host=HOST, port=PORT, db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # 缓存
    SECRET_KEY = 'kdjklfjkd87384hjdhjh'

    # 网易秘钥
    WANGYI_SECRET_ID = "15b731d381bce5120d5a82fa87818484"
    WANGYI_SECRET_KEY = "090be1319d966d926f320681e2069dc1"
    WANGYI_BUSINESSID = "06136123823347ffa6dafebc4311549a"

    # 项目目录
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹的路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 头像的上传目录
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')
    # 相册的上传目录
    UPLOAD_PHOTO_DIR = os.path.join(STATIC_DIR, 'upload/photo')

    # 七牛秘钥私钥
    QINIU_ACCESS_KEY = "IRJpnGmt9BAqCeIwzX2PES5MCOqOE2ivHWWiaAsh"
    QINIU_SECRET_KEY = "ZySl4CPpGv5s5m68t1isIWreWlVwaC6RT3JEATdl"

    # redis缓存
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '101.33.211.216'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 1
    # CACHE_TYPE = 'redis' # 使用redis作为缓存
    CACHE_KEY_PREFIX = "" # 设置cache_key的前缀
    # CACHE_REDIS_HOST  # redis地址
    # CACHE_REDIS_PORT  # redis端口
    # CACHE_REDIS_PASSWORD # redis密码
    # CACHE_REDIS_DB # 使用哪个数据库
    # # 也可以一键配置
    # CACHE_REDIS_URL	连接到Redis服务器的URL。示例redis://user:password@localhost:6379/2
