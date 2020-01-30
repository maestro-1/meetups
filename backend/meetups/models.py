from . import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    imageUrl = db.Column(db.String(25), nullable=False, default="profile.jpg")
    invitation = db.Relationship("Invites", backref="guest", lazy=True)
    meetups = db.Relationship("Events", secondary="links", laszy="subquery",
                              backref=db.backref("meetups", lazy="dynamic"))


class Events(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    invites = db.Relationship("Invites", backref="event", lazy=True)
    imageUrl = db.Column(db.String(25), nullable=False, default="default.jpg")


links = db.Table("links",
                 db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                 db.Column("events_id", db.Integer, db.ForeignKey("events.id"), primary_key=True)
                 )


class Invites(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    guest = db.Column(db.Integer, nullable=False, db.ForeignKey(users.id), uselist=False, unique=True)
    event = db.Column(db.Integer, nullable=False, db.ForeignKey(events.id))
