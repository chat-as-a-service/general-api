from sqlalchemy.orm import Session

from app.models.application import Application


def get_by_name(db: Session, name: str):
    return db.query(Application).filter(Application.name == name).first()


def get_by_id(db: Session, ID: int):
    return db.query(Application).filter(Application.id == ID).first()


def get_all_applications(db: Session):
    return db.query(Application).all()