from sqlalchemy.orm import Session

from app.models.message import Message


def get_by_uuid(db: Session, message_uuid: str):
    return db.query(Message).filter(Message.uuid == message_uuid).first()
