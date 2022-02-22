
from flask import Flask
import logging


class Config:
    DEBUG = False
    ENV = 'production'


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    # logger = logging.getLogger('app')
    # logger.setLevel(level=logging.WARNING)
    # handler = logging.FileHandler('log.txt')
    # handler.setLevel(level=logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='log_new.log',  # 将日志写入log_new.log文件中
                        filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(levelname)s: %(message)s'
                        # 日志格式
                        )
    return app
