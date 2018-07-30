from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "Você deve fazer login para acessar a página"
login_manager.login_view = "signin"
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app.controllers import indexController, bookController, searchController, interestedController, userController, saleController
from app.models import tables



