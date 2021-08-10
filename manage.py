from application import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
app = create_app()
db.init_app(app)
migrate = Migrate(app, db)
