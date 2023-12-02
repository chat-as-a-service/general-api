from sqlalchemy.orm import Session

from app.models.organization import Organization


def get_by_name(db: Session, name: str):
    return db.query(Organization).filter(Organization.name == name).first()


def get_by_id(db: Session, id: int):
    return db.query(Organization).filter(Organization.id == id).first()
