from flask import Flask
from flask_cors import CORS

from api.v1.imcs import api_imc
from api.v1.users import api_user
from db.session import create_db_table

create_db_table()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(api_user)
app.register_blueprint(api_imc)

if __name__ == "__main__":
    app.run(debug=True)
