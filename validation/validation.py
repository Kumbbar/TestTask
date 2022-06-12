from typing import Sequence
from exceptions import InvalidKeysError, InvalidKeyError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
from database.models import Object
from flask import Response
import json


def _validate_key(keys: Sequence) -> None:
    """Check key count and key name"""
    if len(keys) != 1:
        raise InvalidKeyError('Missing key, required key - title')
    if keys[0].lower() != 'title':
        raise InvalidKeyError('Invalid key name, allowed key - title')
    return None


def _validate_keys(keys: Sequence) -> None:
    """Check keys count and key names"""
    if len(keys) != 3:
        raise InvalidKeysError('Missing some keys, required keys - (title, longitude, latitude)')
    for key in keys:
        if key not in ('title', 'longitude', 'latitude'):
            raise InvalidKeysError('Invalid key names, allowed keys - (title, longitude, latitude)')
    return None


def _validate_titles_keys(keys: Sequence) -> None:
    """Check keys count and key names"""
    if len(keys) != 2:
        raise InvalidKeysError('Missing some keys, required keys - '
                               '(first_object_title, second_object_title)')
    for key in keys:
        if key not in ('first_object_title', 'second_object_title'):
            raise InvalidKeysError('Invalid key names, allowed keys - (first_object_title, second_object_title)')
    return None


def _validate_title(title: str) -> None:
    """Check correct title length(no more than 100 and not empty)"""
    if isinstance(title, str) and 0 < len(title) <= 100:
        return None
    raise InvalidValueError('Title length should be no more than 100 and not empty, type - string')


def _validate_longitude(longitude: float) -> None:
    """Check correct longitude type and value(no more than 180 and no less than -180)"""
    if isinstance(longitude, float) and -180 <= longitude <= 180:
        return None
    raise InvalidValueError('Correct longitude value should be no more than 180 and no less than -180, type - float)')


def _validate_latitude(latitude: float) -> None:
    """Check correct latitude type and value(no more than 90 and no less than -90)"""
    if isinstance(latitude, float) and -90 <= latitude <= 90:
        return None
    raise InvalidValueError('Correct latitude value should be no more than 90 and no less than -90, type, float)')


def _validate_all_data(title: str = False, longitude: float = False, latitude: float = False) -> None:
    """Check all data and raise exception"""
    _validate_title(title)
    _validate_longitude(longitude)
    _validate_latitude(latitude)


def check_create_request(json_request) -> (str, float, float):
    """Check create request keys and values, check object exists"""
    _validate_keys(tuple(dict(json_request).keys()))
    title, longitude, latitude = json_request['title'], json_request['longitude'], json_request['latitude']
    _validate_all_data(title, longitude, latitude)
    Object.check_object_exists(title)
    return title, longitude, latitude


def check_get_request(json_request) -> str:
    """Check get request title value and key, check object not exist"""
    _validate_key(tuple(dict(json_request).keys()))
    title = json_request['title']
    _validate_title(title)
    Object.check_object_not_exists(title)
    return title


def check_delete_request(json_request) -> str:
    """Check delete request title value and key, check object not exist"""
    _validate_key(tuple(dict(json_request).keys()))
    title = json_request['title']
    _validate_title(title)
    Object.check_object_not_exists(title)
    return title


def check_edit_request(json_request) -> (str, float, float):
    """Check edit request keys and values, check object not exists"""
    _validate_keys(tuple(dict(json_request).keys()))
    title, longitude, latitude = json_request['title'], json_request['longitude'], json_request['latitude']
    _validate_all_data(title, longitude, latitude)
    Object.check_object_not_exists(title)
    return title, longitude, latitude


def check_calculate_distance_request(json_request) -> (str, str):
    """Check calculate_distance request keys and values, check objects  exists"""
    _validate_titles_keys(tuple(dict(json_request).keys()))
    first_point_title, second_point_title = json_request['first_object_title'], json_request['second_object_title']
    _validate_title(first_point_title)
    _validate_title(second_point_title)
    Object.check_object_not_exists(first_point_title)
    Object.check_object_not_exists(second_point_title)
    return first_point_title, second_point_title
