import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading

from app import creat_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ext import db

app = creat_app()
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)


#
#
# def test(text):
#     t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print('{} --- {}'.format(text, t))
#
#
# def start_job(access_token):
#     scheduler = BlockingScheduler(timezone='Asia/Shanghai')
#     # 每隔 1分钟 运行一次 job 方法
#     scheduler.add_job(func=test, args=[access_token],
#                       trigger="interval", seconds=10)
#     scheduler.start()




if __name__ == '__main__':
    # thread = threading.Thread(target=start_job, args=['666'])
    # thread.start()
    # server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    # server.serve_forever()
    # app.run(host='0.0.0.0', port='8080')
    manager.run()