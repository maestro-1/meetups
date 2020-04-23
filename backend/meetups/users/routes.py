from flask import g, make_response, abort
from meetups import bcrypt, db
from meetups.utils import user_entry
from meetups.models import Users
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from meetups.modelSchema import UserSchema, LoginSchema, UpdateUserSchema
from marshmallow import ValidationError
from pyinstrument import Profiler


users = Blueprint("users", __name__)


@users.before_request
def before_request():
    if "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@users.after_request
def after_request(response):
    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    output = g.profiler.output_text(unicode=True, color=True)
    print(output)
    output_html = g.profiler.output_html()
    return make_response(output_html)


@users.route("/signup", methods=["POST"])
@users.errorhandler(ValidationError)
def sign_up(error=None):
    user_schema = UserSchema()

    try:
        user = user_schema.load(request.json)
        email = Users.query.filter_by(email=user["email"]).first()
        if email:
            raise ValidationError("email address already taken, choose a different one")

        user_entry(user)
        return jsonify("Welcome {}".format(user["password"])), 201
    except ValidationError as error:
        return jsonify({'msg': error.messages}), 400


@users.route("/login", methods=["POST"])
def login():
    from datetime import timedelta
    user_schema = UserSchema()
    login_schema = LoginSchema()
    login = login_schema.load(request.json)
    user = Users.query.filter_by(email=login["email"]).first()
    if user and bcrypt.check_password_hash(user.password, login["password"]):
        access_token = create_access_token(login["email"],
                                           expires_delta=timedelta(hours=24))
        return jsonify(user=user_schema.dump(user), token=access_token)
    return jsonify({'msg': 'Invalid Username or password'}), 400


@users.route('/profile/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def profile(user_id):
    identity = get_jwt_identity()
    user = Users.query.filter_by(email=identity).first()
    update_schema = UpdateUserSchema()

    profile = Users.query.get_or_404(user_id)
    try:
        if request.method == 'GET':
            profile = update_schema.dump(profile)
            return jsonify(profile)

        if request.method == 'PUT' and user.id == user_id:
            update = update_schema.load(request.json)

            user.full_name = update['full_name']
            user.contact = update['contact']
            user.email = update['email']

            db.session.commit()
            return jsonify({'msg': update})

        if request.method == 'DELETE' and user.id == user_id:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg': 'account deleted'}), 203
        else:
            abort(403)

    except ValidationError as error:
        return jsonify({'msg': error.messages}), 400


@users.route('/password_reset', methods=['POST'])
def password_reset(self):
    pass
