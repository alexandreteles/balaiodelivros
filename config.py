import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'balaio.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "199192051312112191512922181519"
            