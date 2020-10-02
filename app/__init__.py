'''
创建app
'''
from flask import Flask
from mysql.connector import connect

from app.config import AppConfig, dbconfig
from app.controllers import users_bp, admin_bp
from app.extensions import db, g
from app.models import *
import os


def create_app(config=AppConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SECRET_KEY'] = os.urandom(24)
    db.init_app(app)

    register_bp(app)
    register_database(app)

    return app


def register_bp(app: Flask):
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_bp)


def register_database(app: Flask):
    @app.before_request
    def startup():
        g.conn = connect(**dbconfig)
        g.cursor = g.conn.cursor()

    @app.after_request
    def teardown(resp):
        g.conn.commit()
        g.cursor.close()
        g.conn.close()
        return resp
