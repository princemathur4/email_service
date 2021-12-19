from flask import Blueprint, jsonify, request
from modules.exceptions import RootException

base_bp = Blueprint('Base', __name__)


@base_bp.app_errorhandler(Exception)
def base_error(e):
    try:
        raise e
    except RootException as er:
        print("Error occurred:", er.internal_err_message)
        return jsonify({'status': False, 'message': er.error_message}), er.http_code
    except Exception as er:
        print("Error occurred:", er.__str__())
        return jsonify({'status': False, 'message': "Something went wrong"}), 500
