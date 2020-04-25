from meetups import db
from meetups.utils import uploads, event_entry
from multiprocessing import Queue, Lock
from meetups.models import Events, Guests, Users
from flask import jsonify, request, Blueprint, g, make_response, abort
from meetups.modelSchema import EventSchema, UpdateUserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional
from werkzeug.exceptions import BadRequestKeyError, NotAcceptable
from pyinstrument import Profiler
from marshmallow import ValidationError

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
    event_schema = EventSchema(many=True, exclude=('guest',))
    # page = request.args.get("page", 1, type=int)
    # events = Events.query.paginate(page=page, per_page=5)
    meetups = Events.query.all()
    meetups = event_schema.dump(meetups)
    return jsonify(meetups), 200


@events.route("/meetup/<int:event_id>")
@jwt_optional
def single_event(event_id):
    user = get_jwt_identity()
    event = Events.query.get_or_404(event_id)
    host_id = event.hosting

    for host in host_id:
        if user and host.email == user:
            event_schema = EventSchema()
            meetups = event_schema.dump(event)
            return jsonify(event=meetups), 200
        continue

    event_schema = EventSchema(exclude=('guest',))
    meetups = event_schema.dump(event)
    return jsonify(event=meetups), 200


@events.route('/meetup/<int:event_id>/edit', methods=['PUT', 'DELETE'])
@jwt_required
def edit_event(event_id):
    identity = get_jwt_identity()
    update_schema = EventSchema()
    events = Events.query.get_or_404(event_id)
    hosts = Users.query.filter(Users.event.any(id=event_id)).all()
    for host in hosts:
        if identity == host.email:

            if request.method == 'PUT' or request.method == 'POST':

                update = update_schema.load(request.json)

                events.title = update['title']
                events.description = update['description']
                events.location = update['location']
                events.date = update['date']

                db.session.commit()
                return jsonify('updated succesfully {}'.format(update))

            try:
                if request.method == 'DELETE':
                    db.session.delete(events)
                    db.session.commit()
                    return jsonify({'msg': 'event deleted'}), 203
            except Exception:
                return jsonify({'msg': 'Try Later'}), 500
    else:
        abort(403)


@events.route("/meetup/create", methods=["POST"])
@jwt_required
def create_event():
    try:
        current_user = get_jwt_identity()
        event_schema = EventSchema()
        event = event_schema.load(request.json)
        host = Users.query.filter_by(email=current_user).first()

        lock.acquire()
        imageUrl = queue.get()
        lock.release()

        if imageUrl == "Not an image":
            return jsonify({'msg': "Not a valid Image"}), 406
        event_entry(event, host, imageUrl)
        return jsonify(event), 201

    except ValidationError as error:
        return jsonify({'msg': error.message}), 400


@events.route("/meetup/create/file", methods=["POST"])
@jwt_required
def file_upload():
    get_jwt_identity()
    try:
        if request.files is not None:
            file_name = uploads(request.files["imageUrl"], "event_image")
            queue.put(file_name)
            return 'done'
        else:
            queue.put("default.jpg")
            return 'done'
    except BadRequestKeyError:
        queue.put("default.jpg")
        return "default.jpg"
