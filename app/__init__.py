# app/__init__.py

import os

# third-party imports
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    my_instance_location = os.path.join(os.path.abspath(os.curdir), 'instance')
    app = Flask(__name__, instance_path=my_instance_location, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    
    Bootstrap(app)

    from app import models

    # blueprint registration
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    # # temporary route
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    # @app.route('/500')
    # def error():
    #     abort(500)

    return app
