import os


class DefaultConfig:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    # 数据库配置
    HOST = '101.33.211.216'
    PORT = '3306'
    DATABASE = 'xhx_flask'
    USERNAME = 'root'
    PASSWORD = '940628'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD,
                                                                               host=HOST, port=PORT, db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # secret_key
    SECRET_KEY = 'kdjklfjkd87384hjdhjh'
    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹的路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


class DevelopmentConfig(DefaultConfig):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(DefaultConfig):
    ENV = 'production'
    DEBUG = False


if __name__ == '__main__':
    print(DefaultConfig.BASE_DIR)
    # print(os.path.abspath(__file__))
    print(DefaultConfig.STATIC_DIR)
