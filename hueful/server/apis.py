from http import HTTPStatus

from flask import Blueprint, request, jsonify

from hueful.Connection import Connection
from hueful.Group import Group
from hueful.Light import Light


def make_rest_api_blueprint() -> Blueprint:
    huey_api_bp = Blueprint('huey', __name__, url_prefix='/api')

    @huey_api_bp.route('/rooms/', methods=['GET'])
    def get_rooms():
        # return JSON of all the rooms
        c = Connection()

        return jsonify(c.get('/groups'))

    @huey_api_bp.route('/rooms/<int:room_id>/', methods=['GET'])
    def get_single_room(room_id):
        # return JSON of just the given room
        c = Connection()

        return jsonify(c.get(f'/groups/{room_id}'))

    @huey_api_bp.route('/rooms/<int:room_id>/state/', methods=['GET'])
    def get_state(room_id):
        c = Connection()
        group = c.get('/groups/1')

        group_state = group['state']

        return jsonify(group_state)

    @huey_api_bp.route('/lights/<int:light_id>/', methods=['GET'])
    def get_light_state(light_id):
        # turn a single line off and on
        c = Connection()
        hue_response = c.get(f'/lights/{light_id}')
        print(hue_response)

        return jsonify(hue_response, HTTPStatus.OK)

    @huey_api_bp.route('/lights/<int:light_id>/state/', methods=['PUT'])
    def set_light_state(light_id):
        # turn a single line off and on
        c = Connection()
        json_data = request.get_json()
        hue_response = c.put(f'/lights/{light_id}/state', json_data)

        return jsonify(hue_response, HTTPStatus.OK)

    @huey_api_bp.route('/rooms/<int:room_id>/action/', methods=['PUT'])
    def turn_room_lights(room_id):
        # return JSON of just the given room
        c = Connection()
        json_data = request.get_json()
        hue_response = c.put(f'/groups/{room_id}/action', json_data)

        return jsonify(hue_response, HTTPStatus.OK)

    return huey_api_bp
