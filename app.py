from api.v1.users import app_user
from db.session import create_db_table

create_db_table()

if __name__ == "__main__":
    app_user.debug = True
    app_user.run(debug=True)
