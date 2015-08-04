from flask import Flask
# from config import ...

app = Flask(__name__)
# app.config.from_object(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from app import views