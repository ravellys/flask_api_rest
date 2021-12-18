from flask import Flask, jsonify, request
from flask_cors import CORS

from db.repository.user import get_users, get_user_by_id, insert_user, update_user, delete_user

app_user = Flask(__name__)
CORS(app_user, resources={r"/*": {"origins": "*"}})


@app_user.route('/api/v1/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())


@app_user.route('/api/v1/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))


@app_user.route('/api/v1/users',  methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))


@app_user.route('/api/v1/users/<user_id>',  methods=['PATCH'])
def api_update_user(user_id):
    user_update = request.get_json()
    return jsonify(update_user(user_update, user_id))


@app_user.route('/api/v1/users/<user_id>',  methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))
