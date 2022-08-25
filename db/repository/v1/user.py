import sqlite3

from db.query.query_user import query_user
from db.session import connect_to_db


def get_users():
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_user.GET_USERS)
        rows = cur.fetchall()

        # convert row objects to dictionary
        users = [dict(row) for row in rows]

    except:
        users = []

    return users


def get_user_by_id(user_id):
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_user.GET_USER_BY_ID, (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user = dict(row)
    except:
        user = {}

    return user


def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_user.INSERT_USER
            , (user['name'], user['email'], user['phone'], user['address'], user['country'])
        )
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)

    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_user


def update_user(user_update, user_id):
    user = get_user_by_id(user_id)
    if not user:
        return {}
    user = {**user, **user_update}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_user.UPDATE_USER_BY_ID,
            (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"],))
        conn.commit()

        #return the user
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute(query_user.DELETE_USER_BY_ID, (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message