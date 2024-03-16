from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from .utils import Status

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
status = Status()


def config_extensions(app: Flask):
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    # 使用cookie
    # cors.init_app(app, supports_credentials=True)

    with app.app_context():
        db.create_all()
