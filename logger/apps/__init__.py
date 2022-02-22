
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
    logging.basicConfig(level=logging.DEBUG,  # ����̨��ӡ����־����
                        filename='log_new.log',  # ����־д��log_new.log�ļ���
                        filemode='a',  # ģʽ����w��a��w����дģʽ��ÿ�ζ�������д��־������֮ǰ����־
                        # a��׷��ģʽ��Ĭ�������д�Ļ�������׷��ģʽ
                        format=
                        '%(asctime)s - %(levelname)s: %(message)s'
                        # ��־��ʽ
                        )
    return app
