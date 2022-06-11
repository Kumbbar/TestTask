from flask import Flask, request, jsonify, Response
from models import db, Object
from peewee import DoesNotExist
from validation import *
from exceptions import KEY_EXCEPTION, KEYS_EXCEPTION, OBJECT_DOES_NOT_EXIST
import json


app = Flask(__name__)


@app.route('/objects/create', methods=['POST'])
def create_object():
    new_object = request.json
    if validate_keys(tuple(dict(new_object).keys())):
        return Response(json.dumps(KEYS_EXCEPTION), status=422, mimetype='application/json')

    title, longitude, latitude = new_object['title'], new_object['longitude'], new_object['latitude']

    if validate_title(title) or validate_longitude(longitude) or validate_latitude(latitude):
        error_message = validate_all_data(title, longitude, latitude)
        return Response(json.dumps({
            'location': [longitude, latitude],
            'message': error_message,
            'error_type': 'InvalidValue'
        }), status=422, mimetype='application/json')

    Object.create(title=title, longitude=longitude, latitude=latitude)
    return Response(json.dumps(new_object), status=201, mimetype='application/json')


@app.route('/objects/get', methods=['GET'])
def get_object():
    data = request.json
    if validate_key(tuple(dict(data).keys())):
        return Response(json.dumps(KEY_EXCEPTION), status=422, mimetype='application/json')

    title = data['title']
    if validate_title(title):
        error_message = validate_all_data(title)
        return Response(json.dumps({
            'message': error_message,
            'error_type': 'InvalidValue'
        }), status=422, mimetype='application/json')

    try:
        result_object = Object.get(title=title)
        if result_object:
            return Response(json.dumps({
                'title': result_object.title,
                'longitude': result_object.longitude,
                'latitude': result_object.latitude
            }), status=422, mimetype='application/json')
    except DoesNotExist as e:
        print(e.__class__.__name__)
        return Response(json.dumps(OBJECT_DOES_NOT_EXIST), status=422, mimetype='application/json')


@app.route('/objects/get_many', methods=['GET'])
def get_many():
    result = []
    objects = Object.select()
    for row in objects:
        result.append({
            'title': row.title,
            'longitude': row.longitude,
            'latitude': row.latitude
        })

    return Response(json.dumps(result), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
