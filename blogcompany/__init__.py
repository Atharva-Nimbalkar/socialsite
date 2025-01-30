from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize extensions without binding to an app yet
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecret'

    # Database setup
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'  # Function name for login route

    # Import blueprints inside the function to avoid circular imports
    from blogcompany.core.views import core
    from blogcompany.error_pages.handlers import error_pages
    from blogcompany.blog_posts.views import blog_posts
    from blogcompany.users.views import users

    # Register blueprints
    app.register_blueprint(core)
    app.register_blueprint(users)
    app.register_blueprint(blog_posts)
    app.register_blueprint(error_pages)

    return app  # Return the configured app instance
