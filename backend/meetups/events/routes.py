from flask import jsonify, request, Blueprint
from meetups import db
from meetups.models import Events, Invites
from meetups.modelSchema import EventSchema


events = Blueprint("events", __name__)


@events.route("/meetups")
def all_events():
    page = request.args.get("page", 1, type=int)
    # events = Events.query.get().paginate(page=page, per_page=5)
    events = Events.query.all()
    return jsonify(events)


@events.route("/meetup/<int:event_id>")
def single_event(event_id):
    events = Events.get_or_404(event_id)
    return jsonify(events)


@events.route("/meetup/create", method=["POST"])
def create_event():
    event_schema = EventSchema()
    event = event_schema.load(request.json)
    event = Events(event)
    db.session.add(event)
    db.session.commit()
    return
