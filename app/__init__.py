from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import basedir

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object('config')

manager = Manager(app)
db = SQLAlchemy(app)
mail = Mail(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from app import views