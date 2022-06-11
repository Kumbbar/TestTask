from typing import Sequence
from exceptions import InvalidKeysError, InvalidKeyError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
from database.models import Object


def _validate_key(keys: Sequence) -> None:
    """Check key count and name"""
    if len(keys) != 1:
        raise InvalidKeyError('Invalid key, allowed key - title')
    if keys[0].lower() != 'title':
        raise InvalidKeyError('Invalid key, allowed key - title')
    return None


def _validate_keys(keys: Sequence) -> None:
    """Check keys count and names"""
    if len(keys) != 3:
        raise InvalidKeysError('Invalid key, allowed keys - (title, longitude, latitude) all required')
    for key in keys:
        if key not in ('title', 'longitude', 'latitude'):
            raise InvalidKeysError('Invalid key, allowed keys - (title, longitude, latitude) all required')
    return None


def _validate_title(title: str) -> None:
    """Check correct title length(no more than 100 and not empty)"""
    if isinstance(title, str) and 0 < len(title) <= 100:
        return None
    raise InvalidValueError('title length should be no more than 100 and not empty, type - string')


def _validate_longitude(longitude: float) -> None:
    """Check correct longitude value(no more than 180 and no less than -180)"""
    if isinstance(longitude, float) and -180 <= longitude <= 180:
        return None
    raise InvalidValueError('correct longitude value should be no more than 180 and no less than -180, type - float)')


def _validate_latitude(latitude: float) -> None:
    """Check correct latitude value(no more than 90 and no less than -90)"""
    if isinstance(latitude, float) and -90 <= latitude <= 90:
        return None
    raise InvalidValueError('correct latitude value should be no more than 90 and no less than -90, type, float)')


def _validate_all_data(title: str = False, longitude: float = False, latitude: float = False) \
        -> None:
    """Get error message for defined error"""
    _validate_title(title)
    _validate_longitude(longitude)
    _validate_latitude(latitude)


def check_create_request(json_request) -> (str, float, float):
    _validate_keys(tuple(dict(json_request).keys()))
    title, longitude, latitude = json_request['title'], json_request['longitude'], json_request['latitude']
    _validate_all_data(title, longitude, latitude)
    Object.check_object_exists(title)
    return title, longitude, latitude


def check_get_request(json_request) -> str:
    _validate_key(tuple(dict(json_request).keys()))
    title = json_request['title']
    _validate_title(title)
    Object.check_object_not_exists(title)
    return title


def check_delete_request(json_request) -> str:
    _validate_key(tuple(dict(json_request).keys()))
    title = json_request['title']
    _validate_title(title)
    Object.check_object_not_exists(title)
    return title


def check_edit_request(json_request) -> (str, float, float):
    _validate_keys(tuple(dict(json_request).keys()))
    title, longitude, latitude = json_request['title'], json_request['longitude'], json_request['latitude']
    _validate_all_data(title, longitude, latitude)
    Object.check_object_not_exists(title)
    return title, longitude, latitude


