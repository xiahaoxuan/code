import datetime

from ext import db


class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义列对象
    id = db.Column(db.INT, primary_key=True, autoincrement=True)  # 主键，自动递增
    username = db.Column(db.String(255), nullable=False) # 不允许为空
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), unique=True)   # 手机号必须唯一
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 默认值
    # # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    # def __repr__(self):
    #     return '<User {}> '.format(self.username)
