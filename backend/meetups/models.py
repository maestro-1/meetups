from . import db


class Users(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    contact = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    imageUrl = db.Column(db.String(25), default="profile.jpg")
    invitation = db.relationship("Invites", backref=db.backref("guest", uselist=False), lazy=True)
    meetups = db.relationship("Events", secondary="links", lazy="subquery",
                              backref=db.backref("meetups", lazy="dynamic"))


class Events(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    imageUrl = db.Column(db.String(25), default="default.jpg")
    invites = db.relationship("Invites", backref="event", lazy=True)


links = db.Table("links",
                 db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                 db.Column("events_id", db.Integer, db.ForeignKey("events.id"), primary_key=True)
                 )


class Invites(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
