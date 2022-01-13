from apps import creat_app
from apps.article.models import *
from apps.user.models import *
from ext import db, bootstrap
from flask_migrate import Migrate

app = creat_app()
db.init_app(app)
bootstrap.init_app(app)

migrate = Migrate(app=app, db=db)

if __name__ == '__main__':
    app.run(port='8080')
