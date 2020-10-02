"""
创建app
"""
from flask import Flask
import click

from app.config import AppConfig
from app.controllers import users_bp, admin_bp
from app.extensions import db, cors
from app.models import *


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    register_extensions(app)
    register_bp(app)
    register_commands(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    cors.init_app(app)


def register_bp(app: Flask):
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_bp)


def register_commands(app: Flask):
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo('Initialized database.')
