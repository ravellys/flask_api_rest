from sqlalchemy.orm import Session

from db.models.users import User


def insert_user(user):
    db = db_session()
    db.add(user)
    db.commit()
    return user
