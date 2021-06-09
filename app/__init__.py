# app/__init__.py


import os
from flask import Flask, render_template, request,session,g
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bootstrap= Bootstrap()

login_manager=LoginManager()
login_manager.login_view='authentication.do_the_login'
login_manager.session_protection='strong'
bcrypt=Bcrypt()



def create_app(config_type ):  # dev, test, prod
    app = Flask(__name__)
    cwd = os.getcwd()
    #config_type1=config_type + '.py'
    #configuration= os.path.join(cwd, 'config', config_type + '.py')

    configuration = os.path.join(cwd, 'config', 'prod' + '.py')

    #'/home/krishna-agrawal/PycharmProjects/book_catalog/config/dev.py'
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main

    app.register_blueprint(main)

    from app.auth import authentication

    app.register_blueprint(authentication)


    return app





