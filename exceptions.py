KEYS_EXCEPTION = {
    'message': 'Invalid key, allowed keys - (title, longitude, latitude) all required',
    'error_type': 'KeyError'
}

KEY_EXCEPTION = {
    'message': 'Invalid key, allowed key - title',
    'error_type': 'KeyError'
}

OBJECT_DOES_NOT_EXIST = {
    'message': 'Object does not exist, try another title',
    'error_type': 'ObjectDoesNotExist'
}

OBJECT_ALREADY_EXISTS = {

}


class InvalidKeysError(Exception):
    pass


class InvalidKeyError(Exception):
    pass


class InvalidValueError(Exception):
    pass


class ObjectDoesNotExistError(Exception):
    pass


class ObjectAlreadyExistsError(Exception):
    pass
