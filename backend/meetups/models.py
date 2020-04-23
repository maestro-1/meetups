from . import db


class Users(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    contact = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    imageUrl = db.Column(db.String(25), default="profile.jpg")


class Events(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    imageUrl = db.Column(db.String(25), default="default.jpg")
    hosting = db.relationship("Users", secondary="hosts", lazy="subquery",
                              backref=db.backref("event", lazy="dynamic"))


hosts = db.Table("hosts",
                 db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                 db.Column("events_id", db.Integer, db.ForeignKey("events.id"), primary_key=True)
                 )


class Guests(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    full_name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    invitation = db.relationship("Events", secondary="guest", lazy="subquery",
                                 backref=db.backref("guest", lazy="dynamic"))


guest = db.Table("guest",
                 db.Column("guests_id", db.Integer, db.ForeignKey("guests.id")),
                 db.Column("events_id", db.Integer, db.ForeignKey("events.id"))
                 )
