from flask_bootstrap import Bootstrap

from apps import creat_app
from ext import db
from flask_migrate import Migrate


app = creat_app()
db.init_app(app)
bootstrap = Bootstrap(app)


migrate = Migrate(app=app, db=db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

