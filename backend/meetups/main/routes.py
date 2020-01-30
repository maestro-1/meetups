from flask import jsonify, Blueprint


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify("managing your events so you don't have to")
