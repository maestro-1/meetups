from meetups.utils import uploads, event_entry
from multiprocessing import Queue, Lock
from meetups.models import Events, Guests
from flask import jsonify, request, Blueprint, g, make_response
from meetups.modelSchema import EventSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequestKeyError, NotAcceptable
from pyinstrument import Profiler

events = Blueprint("events", __name__)
queue = Queue()
lock = Lock()


@events.before_request
def before_request():
    if "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@events.after_request
def after_request(response):
    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    output = g.profiler.output_text(unicode=True, color=True)
    print(output)
    output_html = g.profiler.output_html()
    return make_response(output_html)


@events.route("/meetups")
def all_events():
    event_schema = EventSchema(many=True)
    # page = request.args.get("page", 1, type=int)
    # events = Events.query.paginate(page=page, per_page=5)
    meetups = Events.query.all()
    meetups = event_schema.dump(meetups)

    return jsonify(meetups), 200


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
    # event_entry(event, imageUrl)
    return jsonify(event), 201


@events.route("/meetup/create/file", methods=["POST"])
@jwt_required
def file_upload():
    get_jwt_identity()
    try:
        if request.files is not None:
            file_name = uploads(request.files["imageUrl"], "event_image")
            queue.put(file_name)
            return
    except BadRequestKeyError:
        queue.put("default.jpg")
        return jsonify("default.jpg")
