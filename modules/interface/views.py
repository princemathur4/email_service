from http import HTTPStatus
from flask import Blueprint, jsonify, request
from modules.exceptions import InvalidRequestParams
from .utils import MailServiceUtils

interface_bp = Blueprint('interface', __name__)


@interface_bp.route("/send_mail", methods=['POST'])
def send_mail():
    payload = request.json
    user_name = payload.get("user_name")
    if not user_name or not isinstance(user_name, str):
        raise InvalidRequestParams(internal_err_message="Invalid value for request param: 'user_name'")

    email = payload.get("email")
    if not email or not isinstance(email, str) or not MailServiceUtils.check_email(email=email):
        raise InvalidRequestParams(internal_err_message="Invalid value for request param: 'email'")

    util = MailServiceUtils()
    util.send_email(user_name=user_name, recipient_email=email)
    return jsonify({"status": True, "message": "Mail sent successfully. Please check your inbox."}), HTTPStatus.OK
