import sqlite3
from sqlite3 import IntegrityError
import pandas as pd

from db.query.query_imc import query_imc
from db.session import connect_to_db
from regras_de_negocio.imc import calcular_imc


def get_imcs_from_user(user_id, data):
    if not data:
        return get_imcs_from_user_id(user_id)
    return get_imc_from_user_and_data(user_id, data)


def get_imcs_from_user_id(user_id):
    conn = connect_to_db()

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMCS_FROM_USER, (user_id,))
        rows = cur.fetchall()

        # convert row objects to dictionary
        imcs = [dict(row) for row in rows]

    except:
        imcs = []
    finally:
        conn.close()

    return imcs


def get_imc_from_user_and_data(user_id, data):
    conn = connect_to_db()

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMCS_FROM_USER_AND_DATA, (user_id, data))
        row = cur.fetchone()

        # convert row object to dictionary
        imc = dict(row)
    except:
        imc = {}
    finally:
        conn.close()

    return imc


def get_imc_by_id(imc_id):
    conn = connect_to_db()

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMC_BY_ID, (imc_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        imc = dict(row)
    except:
        imc = {}
    finally:
        conn.close()

    return imc


def insert_imc(imc, user_id):
    conn = connect_to_db()

    try:
        imc['imc'] = calcular_imc(imc['peso'], imc['altura'])
        cur = conn.cursor()
        cur.execute(
            query_imc.INSERT_IMC
            , (imc['data'], imc['altura'], imc['peso'], imc['imc'], user_id)
        )
        conn.commit()
        response = get_imc_by_id(cur.lastrowid)

    except IntegrityError as e:
        response = {
            'message': f"Chave de data {imc['data']}, " +
                       f"precisa ser única, utilize o método PUT para alterar o IMC nesta data"}
    except Exception as e:
        response = {'message': f'ERROR: {e}'}
    finally:
        conn.close()

    return response


def update_imc(imc_update, user_id, data):
    conn = connect_to_db()
    imc = get_imc_from_user_and_data(user_id, data)
    if not imc:
        return {}
    imc = {**imc, **imc_update}
    imc['imc'] = calcular_imc(imc['peso'], imc['altura'])
    try:
        cur = conn.cursor()
        conn.execute(query_imc.UPDATE_IMC,
                     (data, imc['altura'], imc['peso'], imc['imc'], user_id, data))
        conn.commit()

        # return the imc
        updated_imc = get_imc_from_user_and_data(user_id, data)

    except:
        updated_imc = {}
    finally:
        conn.close()

    return updated_imc


def delete_imc(user_id, data):
    conn = connect_to_db()
    message = {}
    try:
        conn.execute(query_imc.DELETE_IMC_FROM_USER_AND_DATA, (user_id, data))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message


def estatisticas_imc(user_id):
    try:
        imcs = get_imcs_from_user_id(user_id)
        df = pd.DataFrame(imcs)
        return df.describe().to_dict()
    except Exception as e:
        return {"message": f"Error: {e}"}
