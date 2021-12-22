from flask import jsonify, request, Blueprint

from db.repository.imc import get_imcs_from_user, get_imc_by_id, insert_imc, update_imc, delete_imc, estatisticas_imc

api_imc = Blueprint('api_imc', __name__)


@api_imc.route('/api/v1/imcs/', methods=['GET'])
def api_get_imcs_from_user_id():
    user_id = request.args.get('user_id')
    data = request.args.get('data')
    return jsonify(get_imcs_from_user(user_id, data))


@api_imc.route('/api/v1/imcs/<user_id>', methods=['POST'])
def api_add_imc(user_id):
    imc = request.get_json()
    return jsonify(insert_imc(imc, user_id))


@api_imc.route('/api/v1/imcs', methods=['PUT'])
def api_update_imc():
    user_id = request.args.get('user_id')
    data = request.args.get('data')
    if not user_id or not data:
        return jsonify({'message': "Operação inválida! É necessário informar uma Data e um id de Usuário"})
    imc_update = request.get_json()
    return jsonify(update_imc(imc_update, user_id, data))


@api_imc.route('/api/v1/imcs', methods=['DELETE'])
def api_delete_imc():
    user_id = request.args.get('user_id')
    data = request.args.get('data')
    if not user_id or not data:
        return jsonify({'message': "Operação inválida! É necessário informar uma Data e um id de Usuário"})
    return jsonify(delete_imc(user_id, data))


@api_imc.route('/api/v1/imcs/estatisticas/<user_id>', methods=['GET'])
def api_estatisticas_imc(user_id):
    return jsonify(estatisticas_imc(user_id))