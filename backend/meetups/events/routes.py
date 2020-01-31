from multiprocessing import Pipe
from meetups import db
from meetups.models import Events, Invites
from flask import jsonify, request, Blueprint
from meetups.modelSchema import EventSchema, uploads


events = Blueprint("events", __name__)
collect, sender = Pipe()


@events.route("/meetups")
def all_events():
    event_schema = EventSchema(many=True)
    page = request.args.get("page", 1, type=int)
    # events = Events.query.get().paginate(page=page, per_page=5)
    meetups = Events.query.all()
    meetups = event_schema.dump(meetups)
    return jsonify(meetups)


@events.route("/meetup/<int:event_id>")
def single_event(event_id):
    events = Events.query.get_or_404(event_id)
    return jsonify(events)


@events.route("/meetup/create", methods=["POST"])
def create_event():
    event_schema = EventSchema()
    event = event_schema.load(request.json)
    imageUrl = collect.recv()
    if imageUrl == "Not an image":
        return jsonify("Not an Image")
    new_event = Events(title=event["title"], description=event["description"],
                       location=event["location"], date=event["date"],
                       imageUrl=imageUrl)
    db.session.add(new_event)
    db.session.commit()
    event["imageUrl"] = imageUrl
    return jsonify(event), 201


@events.route("/meetup/create/file", methods=["POST"])
def file_upload():
    if request.files is not None:
        file = request.files["imageUrl"]
        file_name = uploads(file, "event_image")
        sender.send(file_name)
        sender.close()
        return jsonify("Image received")
