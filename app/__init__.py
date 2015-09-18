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

if app.debug is not True:   
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('moonflask.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

from app import views