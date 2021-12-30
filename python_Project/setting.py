class DefaultConfig:
    ENV = 'devlopment'
    DEBUG = True

    # 数据库配置
    HOST = '101.33.211.216'
    PORT = '3306'
    DATABASE = 'xhx_study'
    USERNAME = 'root'
    PASSWORD = '940628'

    # mysql
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD,
                                                                               host=HOST, port=PORT, db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # redis
    REDIS_HOST = '101.33.211.216'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_EXPIRE = 60

