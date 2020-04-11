from meetups.utils import uploads, event_entry
from multiprocessing import Queue, Lock
from meetups.models import Events, Invites
from flask import jsonify, request, Blueprint
from meetups.modelSchema import EventSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequestKeyError, NotAcceptable

events = Blueprint("events", __name__)
queue = Queue()
lock = Lock()


@events.route("/meetups")
def all_events():
    event_schema = EventSchema(many=True)
    # page = request.args.get("page", 1, type=int)
    # events = Events.query.paginate(page=page, per_page=5)
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
@jwt_required
def create_event():
    current_user = get_jwt_identity()
    event_schema = EventSchema()
    event = event_schema.load(request.json)
    lock.acquire()
    imageUrl = queue.get()
    lock.release()

    if imageUrl == "Not an image":
        raise NotAcceptable("Not an Image")
    event_entry(event, imageUrl)
    return jsonify(event), 201


@events.route("/meetup/create/file", methods=["POST"])
@jwt_required
def file_upload():
    get_jwt_identity()
    try:
        if request.files is not None:
            file_name = uploads(request.files["imageUrl"], "event_image")
            queue.put(file_name)
            return jsonify(file_name)
    except BadRequestKeyError:
        queue.put("default.jpg")
        return jsonify("default.jpg")
