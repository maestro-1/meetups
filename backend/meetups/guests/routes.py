from meetups import db
from meetups.utils import guest_entry
from meetups.models import Events, Guests
from flask import jsonify, request, Blueprint, g, make_response
from meetups.modelSchema import EventSchema, UpdateUserSchema
from werkzeug.exceptions import BadRequestKeyError
from pyinstrument import Profiler
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm.exc import StaleDataError

guests = Blueprint("guests", __name__)


@guests.before_request
def before_request():
    if "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@guests.after_request
def after_request(response):
    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    output = g.profiler.output_text(unicode=True, color=True)
    print(output)
    output_html = g.profiler.output_html()
    return make_response(output_html)


@guests.route("/meetup/<int:event_id>/register", methods=["POST"])
def register_guests(event_id):
    try:
        guest_schema = UpdateUserSchema()
        guest_info = guest_schema.load(request.json)
        guest = Guests.query.filter_by(email=guest_info['email']).first()
        event = Events.query.get_or_404(event_id)

        if guest:
            event.guest.append(guest)
            db.session.commit()
            return jsonify("Registration complete"), 201

        guest_entry(guest_info, event)
        return jsonify("Registration complete"), 201

    except ValidationError as error:
        return jsonify({'msg': error.messages}), 400
    except BadRequestKeyError:
        return jsonify('bad request key'), 400
    except IntegrityError:
        return jsonify('Already registered'), 200


@guests.route("/meetup/<int:event_id>/unregister", methods=["POST"])
def unregister_guest(event_id):
    guest_schema = UpdateUserSchema()
    event = Events.query.get_or_404(event_id)
    guest_info = guest_schema.load(request.json)
    guest = Guests.query.filter_by(email=guest_info['email']).first()

    if not guest:
        return jsonify('you are not registered'), 200

    registered = Guests.query.filter(Guests.invitation.any(id=event_id)).all()
    for register in registered:
        if register.email == guest.email:
            event.guest.remove(guest)
            db.session.commit()
            return jsonify('You have been unregistered for this event'), 200
    return jsonify('you are not registered'), 200
