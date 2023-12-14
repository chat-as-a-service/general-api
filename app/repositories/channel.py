from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.channel import Channel
from app.models.channel_users import channel_users
from app.models.message import Message


def get_by_name(db: Session, name: str):
    return db.query(Channel).filter(Channel.name == name).first()


def get_by_application_id_and_channel(
    db: Session, application_id: int, channelName: str
):
    return (
        db.query(Channel)
        .filter(
            Channel.application_id == application_id and Channel.name == channelName
        )
        .first()
    )


def list_channels_with_user_count(
    application_id: int, search_keyword: str, db: Session
):
    return (
        db.query(
            Channel,
            func.count(channel_users.c.user_id).label("user_count"),
        )
        .outerjoin(channel_users, Channel.id == channel_users.c.channel_id)
        .filter(
            Channel.application_id == application_id,
            Channel.name.like(f"{search_keyword}%"),
        )
        .group_by(Channel.id)
        .order_by(Channel.created_at.desc())
        .all()
    )


def list_channel_ids_with_last_message_at(
    application_id: int, search_keyword: str, db: Session
):
    return (
        db.query(
            Channel.id,
            func.max(Message.created_at).label("last_message_at"),
        )
        .join(Message, Channel.id == Message.channel_id)
        .filter(
            Channel.application_id == application_id,
            Channel.name.like(f"{search_keyword}%"),
        )
        .group_by(Channel.id)
        .all()
    )
