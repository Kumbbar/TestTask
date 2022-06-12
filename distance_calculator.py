from config import OPEN_ROUTE_SERVICE_TOKEN
from database.models import Object
import requests
from geopy.distance import geodesic


def get_distance_between_two_objects(first_object: Object, second_object: Object) -> float:
    """Calculate distance between two objects with open_route_service API or geopy"""
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json',
        'Authorization': OPEN_ROUTE_SERVICE_TOKEN
    }

    data = {"coordinates": [[first_object.longitude, first_object.latitude],
                            [second_object.longitude, second_object.latitude]], "units": "km"}

    response = requests.post(f'https://api.openrouteservice.org/v2/directions/foot-walking',
                             headers=headers,
                             json=data).json()
    # use geopy if open_route_service returned error
    if 'routes' in response.keys():
        distance = response['routes'][0]['summary']['distance']
    else:
        distance = geodesic((first_object.latitude, first_object.longitude),
                            (second_object.latitude, second_object.longitude)).kilometers
    return distance
