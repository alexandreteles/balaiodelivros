import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'balaio.db')
WHOOSH_BASE = os.path.join(basedir, 'balaio.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = "199192051312112191512922181519"
MAX_SEARCH_RESULTS = 10
