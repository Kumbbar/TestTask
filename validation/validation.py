from exceptions import InvalidValueError
from database.models import Object
from pydantic import BaseModel, validator


class ObjectModelGetDelete(BaseModel):
    title: str

    @validator('title')
    def validate_title(cls, v):
        if 0 < len(v) <= 150:
            return v
        raise ValueError('Title length should be no more than 100 and not empty, type - string')


class ObjectModelCreateEdit(ObjectModelGetDelete):
    longitude: float
    latitude: float

    @validator('longitude')
    def validate_longitude(cls, v):
        if -180 <= v <= 180:
            return v
        raise ValueError('Correct longitude value should be no more' +
                         'than 180 and no less than -180, type - float)')

    @validator('latitude')
    def validate_latitude(cls, v):
        if -90 <= v <= 90:
            return v
        raise ValueError('Correct latitude value should be no more than 90 and no less than -90, type, float)')


class ObjectModelCalculate(BaseModel):
    first_object_title: str
    second_object_title: str

    @validator('first_object_title')
    def validate_first_object_title(cls, v):
        if 0 < len(v) <= 150:
            return v
        raise ValueError('Title length should be no more than 100 and not empty, type - string')

    @validator('second_object_title')
    def validate_second_object_title(cls, v):
        if 0 < len(v) <= 150:
            return v
        raise ValueError('Title length should be no more than 100 and not empty, type - string')


def check_create_request(json_request) -> (str, float, float):
    """Check create request keys and values, check object exists"""
    data = ObjectModelCreateEdit.parse_raw(json_request)
    title, longitude, latitude = data.title, data.longitude, data.latitude
    Object.check_object_exists(title)
    return title, longitude, latitude


def check_get_request(json_request) -> str:
    """Check get request title value and key, check object not exist"""
    data = ObjectModelGetDelete.parse_raw(json_request)
    title = data.title
    Object.check_object_not_exists(title)
    return title


def check_delete_request(json_request) -> str:
    """Check delete request title value and key, check object not exist"""
    data = ObjectModelGetDelete.parse_raw(json_request)
    title = data.title
    Object.check_object_not_exists(title)
    return title


def check_edit_request(json_request) -> (str, float, float):
    """Check edit request keys and values, check object not exists"""
    data = ObjectModelCreateEdit.parse_raw(json_request)
    title, longitude, latitude = data.title, data.longitude, data.latitude
    Object.check_object_not_exists(title)
    return title, longitude, latitude


def check_calculate_distance_request(json_request) -> (str, str):
    """Check calculate_distance request keys and values, check objects  exists"""
    data = ObjectModelCalculate.parse_raw(json_request)
    first_point_title, second_point_title = data.first_object_title, data.second_object_title
    Object.check_object_not_exists(first_point_title)
    Object.check_object_not_exists(second_point_title)
    return first_point_title, second_point_title
