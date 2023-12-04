from sqlalchemy.orm import Session

from app.models.channel import Channel


def get_by_name(db: Session, name: str):
    return db.query(Channel).filter(Channel.name == name).first()
