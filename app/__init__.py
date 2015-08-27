from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Shell
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
manager = Manager(app)
db = SQLAlchemy(app)

from app import views