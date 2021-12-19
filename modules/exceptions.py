from http import HTTPStatus


class RootException(Exception):
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_message = "Something went wrong"
    internal_err_message = "Something went wrong"
    error_code = '100'


class InvalidRequestParams(RootException):
    error_code = '101'
    internal_err_message = 'Invalid request params/payload'
    error_message = 'Invalid request params/payload'
    http_code = HTTPStatus.BAD_REQUEST

    def __init__(self, internal_err_message):
        self.internal_err_message = internal_err_message


class InvalidInputParameter(RootException):
    error_code = '102'
    internal_err_message = 'Invalid argument'
    error_message = 'Something went wrong.'

    def __init__(self, internal_err_message):
        self.internal_err_message = internal_err_message


class EmailNotSent(RootException):
    error_code = '103'
    internal_err_message = "Couldn't send email"
    error_message = "Couldn't send email"

    def __init__(self, internal_err_message):
        self.internal_err_message = internal_err_message
