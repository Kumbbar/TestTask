from exceptions import InvalidKeyError, InvalidKeysError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
from flask import Response
import json


def except_validation_error_decorator(func):
    """Except all custom exception and return error data to user"""
    def wrapper():
        try:
            response = func()
            return response
        except (InvalidKeyError, InvalidKeysError, InvalidValueError, ObjectDoesNotExistError,
                ObjectAlreadyExistsError) as e:
            return Response(json.dumps({
                'message': str(e),
                'error_type': str(e.__class__.__name__)
            }), status=422, mimetype='application/json')
    wrapper.__name__ = func.__name__
    return wrapper
