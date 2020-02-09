import asyncio
from meetups import bcrypt
from meetups.utils import user_entry
from meetups.models import Users
from flask import jsonify, request, Blueprint
from meetups.modelSchema import UserSchema
from marshmallow import ValidationError

users = Blueprint("users", __name__)


@users.route("/signup", methods=["POST"])
def sign_up():
    user_schema = UserSchema()
    user = user_schema.load(request.json)
    email = Users.query.filter_by(email=user["email"]).first()
    if email:
        raise ValidationError("email address already taken, choose a different one")
    asyncio.run(user_entry(user))
    return jsonify("Welcome {}".format(user["fullname"]))


@users.route("/login", methods=["POST"])
def sign_in():
    user_schema = UserSchema()
    user = user_schema.load(request.json)
    Users.query.filter_by(email=user["email"]).first()
    if user and bcrypt.check_password_hash(user.password, user["password"]):
        pass
        return jsonify("")
    else:
        raise ValidationError("invalid email or password")
