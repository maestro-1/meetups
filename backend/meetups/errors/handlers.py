from flask import jsonify, Blueprint


errors = Blueprint("errors", __name__)


@errors.app_errorhandler(500)
def error_500(error):
    return jsonify('Internal Serve Error'), 500


@errors.app_errorhandler(404)
def error_404(error):
    return jsonify('Resource was not found'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return jsonify('Forbidden, you do not have authorization'), 403


@errors.app_errorhandler(401)
def error_401(error):
    return jsonify('Unauthorized, login to access resource'), 401
