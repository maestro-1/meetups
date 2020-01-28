from flask import jsonify, request
from . import app, bcrypt


@app.route("/")
def home():
    return jsonify("Hello There")
