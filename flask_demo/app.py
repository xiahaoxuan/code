import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading

from apps import creat_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ext import db
from apps.user.models import User

app = creat_app()

# manager = Manager(app=app)
# migrate = Migrate(app=app, db=db)
#
# manager.add_command('db', MigrateCommand)


if __name__ == '__main__':

    # server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    # server.serve_forever()
    app.run(host='0.0.0.0', port='8080')
    # manager.run()
    # with app.app_context():
    #     db.create_all()
