
from apps.user.models import *
from apps import creat_app
from flask_migrate import Migrate

app = creat_app()
migrate = Migrate(app=app, db=db)

if __name__ == '__main__':
    app.run()
