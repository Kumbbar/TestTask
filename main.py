from flask import Flask, request, Response
import json
from validation.validation import check_create_request, check_get_request, check_edit_request, check_delete_request, \
    check_calculate_distance_request
from validation.decorators import except_validation_error_decorator
from database.models import Object
from distance_calculator import get_distance_between_two_objects


app = Flask(__name__)


@app.route('/objects/create', methods=['POST'])
@except_validation_error_decorator
def create_object() -> Response:
    """Create new object in database with data from json request"""
    new_object = request.json
    title, longitude, latitude = check_create_request(json.dumps(new_object))
    Object.create(title=title, longitude=longitude, latitude=latitude)
    return Response(json.dumps(new_object), status=201, mimetype='application/json')


@app.route('/objects/get', methods=['POST'])
@except_validation_error_decorator
def get_object() -> Response:
    """Get object from database by title from json request"""
    data = request.json
    title = check_get_request(json.dumps(data))
    result_object = Object.get(title=title)

    return Response(json.dumps({
        'title': result_object.title,
        'longitude': result_object.longitude,
        'latitude': result_object.latitude
    }), status=200, mimetype='application/json')


@app.route('/objects/get_many', methods=['POST'])
def get_many_objects() -> Response:
    """Return all objects in database"""
    result = []
    objects = Object.select()
    for row in objects:
        result.append({
            'title': row.title,
            'longitude': row.longitude,
            'latitude': row.latitude
        })
    return Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/objects/edit', methods=['POST'])
@except_validation_error_decorator
def edit_object() -> Response:
    """Edit object longitude and latitude in database by title from json request"""
    target_object = request.json
    title, longitude, latitude = check_edit_request(json.dumps(target_object))

    modified_object = Object.select().where(Object.title == title).get()
    modified_object.longitude = longitude
    modified_object.latitude = latitude
    modified_object.save()
    return Response(json.dumps(target_object), status=200, mimetype='application/json')


@app.route('/objects/delete', methods=['POST'])
@except_validation_error_decorator
def delete_object() -> Response:
    """Delete object from database by title from json request"""
    data = request.json
    title = check_delete_request(json.dumps(data))

    deleted_object = Object.select().where(Object.title == title).get()
    Object.delete().where(Object.title == title).execute()
    return Response(json.dumps({
        'title': deleted_object.title,
        'longitude': deleted_object.longitude,
        'latitude': deleted_object.latitude
    }), status=200, mimetype='application/json')


@app.route('/objects/calculate_distance', methods=['POST'])
@except_validation_error_decorator
def calculate_distance() -> Response:
    """Calculate distance between two objects from database by titles from json request"""
    titles = request.json
    first_object_title, second_second_title = check_calculate_distance_request(json.dumps(titles))

    first_object = Object.get(title=first_object_title)
    second_object = Object.get(title=second_second_title)
    distance = get_distance_between_two_objects(first_object, second_object)
    return Response(json.dumps({
        "title": f"Response Calculate Distance between {first_object_title} and {second_second_title} " +
        "in kilometers",
        "distance": round(distance, 4)
    }), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=False)
