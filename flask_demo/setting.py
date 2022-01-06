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