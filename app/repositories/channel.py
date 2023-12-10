from sqlalchemy.orm import Session

from app.models.channel import Channel


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


def get_all_channel_list(db: Session):
    return db.query(Channel).all()
