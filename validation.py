from typing import Sequence
from exceptions import InvalidKeysError, InvalidKeyError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
from models import Object


def validate_key(keys: Sequence) -> None:
    """Check key count and name"""
    if len(keys) != 1:
        raise InvalidKeyError('Invalid key, allowed key - title')
    if keys[0].lower() != 'title':
        raise InvalidKeyError('Invalid key, allowed key - title')
    return None


def validate_keys(keys: Sequence) -> None:
    """Check keys count and names"""
    if len(keys) != 3:
        raise InvalidKeysError('Invalid key, allowed keys - (title, longitude, latitude) all required')
    for key in keys:
        if key not in ('title', 'longitude', 'latitude'):
            raise InvalidKeysError('Invalid key, allowed keys - (title, longitude, latitude) all required')
    return None


def validate_title(title: str) -> None:
    """Check correct title length(no more than 100 and not empty)"""
    if isinstance(title, str) and 0 < len(title) <= 100:
        return None
    raise InvalidValueError('title length should be no more than 100 and not empty, type - string')


def validate_longitude(longitude: float) -> None:
    """Check correct longitude value(no more than 180 and no less than -180)"""
    if isinstance(longitude, float) and -180 <= longitude <= 180:
        return None
    raise InvalidValueError('correct longitude value should be no more than 180 and no less than -180, type - float)')


def validate_latitude(latitude: float) -> bool:
    """Check correct latitude value(no more than 90 and no less than -90)"""
    if isinstance(latitude, float) and -90 <= latitude <= 90:
        return False
    raise InvalidValueError('correct latitude value should be no more than 90 and no less than -90, type, float)')


def validate_all_data(title: str = False, longitude: float = False, latitude: float = False) \
        -> None:
    """Get error message for defined error"""
    validate_title(title)
    validate_longitude(longitude)
    validate_latitude(latitude)


def check_object_exists(title: str) -> None:
    items_titles = [row.title for row in Object.select()]
    if title in items_titles:
        raise ObjectAlreadyExistsError('object with this name already exists, try another title')


def check_object_not_exists(title: str) -> None:
    items_titles = [row.title for row in Object.select()]
    if title not in items_titles:
        raise ObjectDoesNotExistError('object does not exist, try another title')
