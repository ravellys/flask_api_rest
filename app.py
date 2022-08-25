from flask import Flask
from flask_cors import CORS

from api.v1.imcs import api_imc
from api.v1.users import api_user
from db.models.base_class import db, Base
from db.session import engine, create_db_table


def create_tables():
    Base.metadata.create_all(bind=engine)


def register_blueprint(app: Flask):
    app.register_blueprint(api_user)
    app.register_blueprint(api_imc)


def create_app():

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    create_db_table()
    register_blueprint(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()

# flask db migrate
# flask db upgrade
