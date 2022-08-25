from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask("rw-trains")
app.config.from_object('settings.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)