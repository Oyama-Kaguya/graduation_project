from flask import Blueprint, request, jsonify

from ..extensions import db
from ..services.user import UserORMHandler, UserDetailORMHandler

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("", methods=["GET"])
def get_user():
    return "123456"


@user_blueprint.route("", methods=["POST"])
def login():
    data = request.get_json()
    access_token = "123456"
    return jsonify(access_token='Bearer ' + access_token) \
        if UserORMHandler(db.session).login(**data) else \
        (jsonify(msg="Bad username or password"), 401)
