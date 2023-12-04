from sqlalchemy.orm import Session

from app.models.user import User

def get_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_by_application_id_and_username(db: Session, application_id: int, username: str):
    return db.query(User).filter(User.application_id == application_id and User.username == username).first()
