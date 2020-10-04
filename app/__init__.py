"""
创建app
"""
from flask import Flask, jsonify
import click

from app.config import AppConfig
from app.controllers import users_bp, admin_bp
from app.extensions import db, cors
from app.models import *
from app.middlewares import before_request
from app.extends.error import HttpError


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    register_extensions(app)
    register_middleware(app)
    register_errorhandler(app)
    register_bp(app)
    register_commands(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    cors.init_app(app)


def register_middleware(app: Flask):
    users_bp.before_request(before_request)


def register_errorhandler(app: Flask):
    @app.errorhandler(HttpError)
    def handle_http_error(error: HttpError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def register_bp(app: Flask):
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_bp)


def register_commands(app: Flask):
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo('Initialized database.')
