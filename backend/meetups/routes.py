from flask import jsonify, request
from . import app, bcrypt, db
from .models import Users, Events, Invites


@app.route("/")
def home():
    return jsonify("Hello There")


@app.route("/meetups")
def all_events():
    return jsonify("Hello There")


@app.route("/meetup")
def single_event():
    return jsonify("Hello There")


@app.route("/meetup/create")
def create_event():
    title = request.form["title"]
    location = request.form["location"]
    description = request.form["description"]
    date = request.form["date"]
    event = Events()
    db.session.add(event)
    db.session.commit()
    return jsonify()
