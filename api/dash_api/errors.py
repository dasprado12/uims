from flask import jsonify, Blueprint

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(400)
def bad_request(error):
    return jsonify({'code': 400, 'message': 'Bad Request',
                    'details': 'The request could not be understood by '
                    'the server due to malformed syntax. The client SHOULD'
                    ' NOT repeat the request without modifications.'}), 400


@error_handler.app_errorhandler(422)
def client_or_service_not_found(error):
    return jsonify({'code': 422, 'message': error.description['message'],
                    'details': error.description['details']}), 422
