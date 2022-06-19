from exceptions import InvalidKeyError, InvalidKeysError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
from flask import Response
import json
from pydantic import ValidationError


def except_validation_error_decorator(func):
    """Except all custom exception and return error data to user"""
    def wrapper():
        try:
            response = func()
            return response
        except (ObjectDoesNotExistError, ObjectAlreadyExistsError,) as e:
            return Response(json.dumps({
                'message': str(e),
                'error_type': str(e.__class__.__name__)
            }), status=422, mimetype='application/json')
        except ValueError as e:
            return Response(e.json(), status=422, mimetype='application/json')
    wrapper.__name__ = func.__name__
    return wrapper
