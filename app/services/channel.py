from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.channel import Channel
from app.repositories.channel import get_by_name, get_all_channel_list
from app.schemas.channel import ChannelCreate, ChannelCreateResponse


async def create_channel(dto: ChannelCreate, db: Session):
    new_channel = Channel(
        application_id=dto.application_id,
        name=dto.name,
        # TODO: should discuss Daniel what this Max_members value should be?
        max_members=100,
        created_by="system",
        updated_by="system",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    new_channel_response = ChannelCreateResponse(
        name=new_channel.name, application_id=new_channel.application_id
    )
    return new_channel_response


async def view_channel(db: Session, name: str):
    if not get_by_name(db, name):
        return {"error": "the channel does not exist"}

    return get_by_name(db, name)


async def list_channel(db: Session):
    channels = get_all_channel_list(db)

    return channels
