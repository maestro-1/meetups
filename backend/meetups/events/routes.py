import asyncio
from meetups.utils import uploads, datebase_entry
from multiprocessing import Queue, Lock
from meetups.models import Events, Invites
from flask import jsonify, request, Blueprint
from meetups.modelSchema import EventSchema
from werkzeug.exceptions import BadRequestKeyError, NotAcceptable

events = Blueprint("events", __name__)
queue = Queue()
lock = Lock()


@events.route("/meetups")
def all_events():
    event_schema = EventSchema(many=True)
    # page = request.args.get("page", 1, type=int)
    # events = Events.query.get().paginate(page=page, per_page=5)
    meetups = Events.query.all()
    meetups = event_schema.dump(meetups)
    return jsonify(meetups)


@events.route("/meetup/<int:event_id>")
def single_event(event_id):
    event_schema = EventSchema()
    event = Events.query.get_or_404(event_id)
    event = event_schema.dump(event)
    return jsonify(event)


@events.route("/meetup/create", methods=["POST"])
def create_event():
    event_schema = EventSchema()
    event = event_schema.load(request.json)
    lock.acquire()
    imageUrl = queue.get()
    lock.release()

    if imageUrl == "Not an image":
        raise NotAcceptable("Not an Image")
    asyncio.run(datebase_entry(event, imageUrl))
    return jsonify("created"), 201


@events.route("/meetup/create/file", methods=["POST"])
def file_upload():
    try:
        if request.files is not None:
            file_name = uploads(request.files["imageUrl"], "event_image")
            queue.put(file_name)
            return jsonify("Done")
    except BadRequestKeyError:
        queue.put("default.jpg")
        return jsonify("Done")
