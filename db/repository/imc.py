import sqlite3
from datetime import datetime

from db.query.query_imc import query_imc
from db.session import connect_to_db
from regras_de_negocio.imc import calcular_imc


def get_imcs_from_user_id(user_id):
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMCS_FROM_USER_ID, (user_id,))
        rows = cur.fetchall()

        # convert row objects to dictionary
        imcs = [dict(row) for row in rows]

    except:
        imcs = []

    return imcs


def get_imc_by_id(imc_id):
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMC_BY_ID, (imc_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        imc = dict(row)
    except:
        imc = {}

    return imc


def insert_imc(imc):
    inserted_imc = {}
    try:
        imc['imc'] = calcular_imc(imc['peso'], imc['altura'])

        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_imc.INSERT_IMC
            , (imc['data'], imc['altura'], imc['peso'], imc['imc'], imc['user_id'])
        )
        conn.commit()
        inserted_imc = get_imc_by_id(cur.lastrowid)

    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_imc


def update_imc(imc_update, imc_id):
    imc = get_imc_by_id(imc_id)
    if not imc:
        return {}
    imc = {**imc, **imc_update}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_imc.UPDATE_USER_BY_ID,
            (imc["name"], imc["email"], imc["phone"], imc["address"], imc["country"], imc["imc_id"],))
        conn.commit()

        # return the imc
        updated_imc = get_imc_by_id(imc["imc_id"])

    except:
        conn.rollback()
        updated_imc = {}
    finally:
        conn.close()

    return updated_imc


def delete_imc(imc_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute(query_imc.DELETE_IMC_BY_ID, (imc_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message
