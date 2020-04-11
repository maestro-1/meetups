from flask import after_this_request
from meetups import bcrypt
from meetups.utils import user_entry
from meetups.models import Users
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token
from meetups.modelSchema import UserSchema, LoginSchema
from marshmallow import ValidationError

users = Blueprint("users", __name__)


@users.route("/signup", methods=["POST"])
def sign_up():
    user_schema = UserSchema()
    user = user_schema.load(request.json)
    email = Users.query.filter_by(email=user["email"]).first()
    if email:
        raise ValidationError("email address already taken, choose a different one")
    user_entry(user)
    return jsonify("Welcome {}".format(user["full_name"]))


@users.route("/login", methods=["POST"])
def sign_in():
    from datetime import timedelta
    user_schema = UserSchema()
    login_schema = LoginSchema()
    login = login_schema.load(request.json)
    user = Users.query.filter_by(email=login["email"]).first()
    if user and bcrypt.check_password_hash(user.password, login["password"]):
        access_token = create_access_token(login["email"],
                                           expires_delta=timedelta(hours=24))

        @after_this_request
        def authorization_header(response):
            response.headers["Authorization"] = access_token
            print(response.headers)
            return response
        return jsonify(user_schema.dump(user), access_token)
    return jsonify({'msg': 'Invalid Username or password'}), 400
