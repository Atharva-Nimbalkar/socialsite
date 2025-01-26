from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY ']='mysecret'
#db setup
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

#login config
login_manager=LoginManager()

login_manager.init_app(app)
login_manager.login_view='users.login'#function name of the route that handles login page 


from blogcompany.core.views import core
from blogcompany.error_pages.handlers import error_pages
from blogcompany.users.views import users

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)