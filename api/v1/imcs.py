from flask import jsonify, request, Blueprint

from db.repository.imc import get_imcs_from_user_id, get_imc_by_id, insert_imc, update_imc, delete_imc

api_imc = Blueprint('api_imc', __name__)


@api_imc.route('/api/v1/imcs/<user_id>', methods=['GET'])
def api_get_imcs_from_user_id(user_id):
    return jsonify(get_imcs_from_user_id(user_id))


@api_imc.route('/api/v1/imcs/<imc_id>', methods=['GET'])
def api_get_imc(imc_id):
    return jsonify(get_imc_by_id(imc_id))


@api_imc.route('/api/v1/imcs', methods=['POST'])
def api_add_imc():
    imc = request.get_json()
    return jsonify(insert_imc(imc))


@api_imc.route('/api/v1/imcs/<imc_id>', methods=['PATCH'])
def api_update_imc(imc_id):
    imc_update = request.get_json()
    return jsonify(update_imc(imc_update, imc_id))


@api_imc.route('/api/v1/imcs/<imc_id>', methods=['DELETE'])
def api_delete_imc(imc_id):
    return jsonify(delete_imc(imc_id))
