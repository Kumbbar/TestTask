
def check_key(keys: list) -> bool:
    """Check key count and name"""
    if len(keys) != 1:
        return True
    if keys[0].lower() != 'title':
        return True
    return False


def check_keys(keys: list) -> bool:
    """Check keys count and names"""
    if len(keys) != 3:
        return True
    for key in keys:
        if key not in ('title', 'longitude', 'latitude'):
            return True
    return False


def check_title(title: str) -> bool:
    """Check correct title length(no more than 100 and not empty)"""
    if isinstance(title, str) and 0 < len(title) <= 100:
        return False
    return True


def check_longitude(longitude: float) -> bool:
    """Check correct longitude value(no more than 180 and no less than -180)"""
    if isinstance(longitude, float) and -180 <= longitude <= 180:
        return False
    return True


def check_latitude(latitude: float) -> bool:
    """Check correct latitude value(no more than 90 and no less than -90)"""
    if isinstance(latitude, float) and -90 <= latitude <= 90:
        return False
    return True


def check_all_errors_and_get_error_message(title: str = False, longitude: float = False, latitude: float = False) \
        -> str:
    """Get error message for defined error"""
    if check_title(title):
        return "title length should be no more than 100 and not empty, type - string"
    if check_longitude(longitude):
        return "correct longitude value should be no more than 180 and no less than -180, type - float)"
    if check_latitude(latitude):
        return "correct latitude value should be no more than 90 and no less than -90, type, float)"
