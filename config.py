import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SECRET_KEY = os.environ.get('SECRET_KEY') or 'Crazy string that you must put into an environment variable'

MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MOON_MAIL_SUBJECT_PREFIX = '[Moon-Flask] '
