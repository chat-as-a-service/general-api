from typing import List

from sqlalchemy import or_, delete
from sqlalchemy.orm import Session

from app.models.user import User


def get_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_by_application_id_and_username(db: Session, application_id: int, username: str):
    return (
        db.query(User)
        .filter(User.application_id == application_id, User.username == username)
        .first()
    )


def get_by_username(db: Session, name: str):
    return db.query(User).filter(User.username == name).first()


def get_all_users_in_app(application_id: int, search_keyword: str, db: Session):
    return (
        db.query(User)
        .filter(
            User.application_id == application_id,
            or_(
                User.username.like(f"{search_keyword}%"),
                User.nickname.like(f"{search_keyword}%"),
            ),
        )
        .all()
    )


def delete_users(application_id: int, usernames: List[str], db: Session):
    query = (
        delete(User)
        .where(User.application_id == application_id, User.username.in_(usernames))
        .returning(User.username)
    )
    return db.execute(query).fetchall()
