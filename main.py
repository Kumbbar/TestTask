from flask import Flask, request, Response
from validation import *
from exceptions import InvalidKeysError, InvalidKeyError, InvalidValueError, ObjectDoesNotExistError, \
    ObjectAlreadyExistsError
import json
from database.models import Object

app = Flask(__name__)


@app.route('/objects/create', methods=['POST'])
def create_object() -> Response:
    new_object = request.json
    try:
        title, longitude, latitude = check_create_request(new_object)

        Object.create(title=title, longitude=longitude, latitude=latitude)
        return Response(json.dumps(new_object), status=201, mimetype='application/json')

    except (InvalidKeysError, InvalidValueError, ObjectAlreadyExistsError) as e:
        return Response(json.dumps({
            'message': str(e),
            'error_type': str(e.__class__.__name__)
        }), status=422, mimetype='application/json')


@app.route('/objects/get', methods=['GET'])
def get_object() -> Response:
    data = request.json
    try:
        title = check_get_request(data)
        result_object = Object.get(title=title)

        return Response(json.dumps({
            'title': result_object.title,
            'longitude': result_object.longitude,
            'latitude': result_object.latitude
        }), status=200, mimetype='application/json')

    except (InvalidKeyError, InvalidValueError, ObjectDoesNotExistError) as e:
        return Response(json.dumps({
            'message': str(e),
            'error_type': str(e.__class__.__name__)
        }), status=422, mimetype='application/json')


@app.route('/objects/get_many', methods=['GET'])
def get_many_objects():
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
def edit_object():
    target_object = request.json
    try:
        title, longitude, latitude = check_edit_request(target_object)

        modified_object = Object.select().where(Object.title == title).get()
        modified_object.longitude = longitude
        modified_object.latitude = latitude
        modified_object.save()

        return Response(json.dumps(target_object), status=200, mimetype='application/json')
    except (InvalidKeysError, InvalidValueError, ObjectDoesNotExistError ) as e:
        return Response(json.dumps({
            'message': str(e),
            'error_type': str(e.__class__.__name__)
        }), status=422, mimetype='application/json')


@app.route('/objects/delete', methods=['GET'])
def delete_object() -> Response:
    data = request.json
    try:
        title = check_delete_request(data)

        deleted_object = Object.select().where(Object.title == title).get()
        Object.delete().where(Object.title == title).execute()

        return Response(json.dumps({
            'title': deleted_object.title,
            'longitude': deleted_object.longitude,
            'latitude': deleted_object.latitude
        }), status=200, mimetype='application/json')

    except (InvalidKeyError, InvalidValueError, ObjectDoesNotExistError) as e:
        return Response(json.dumps({
            'message': str(e),
            'error_type': str(e.__class__.__name__)
        }), status=422, mimetype='application/json')


@app.route('/objects/calculate_distance', methods=['GET'])
def calculate_distance() -> Response:
    pass


if __name__ == '__main__':
    app.run(debug=True)
