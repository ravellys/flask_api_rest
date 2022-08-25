import sqlite3

from sqlalchemy import create_engine

from db.query.query_imc import query_imc
from db.query.query_user import query_user


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()

        conn.execute(query_user.CREATE_TABLE_USERS)
        print(">>> User table created successfully")

        conn.execute(query_imc.CREATE_TABLE_IMCS)
        print(">>> IMC table created seccessfully")

        conn.commit()
    except:
        print(">>> User table creation failed - Maybe table")
    finally:
        conn.close()


# conectar com sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)