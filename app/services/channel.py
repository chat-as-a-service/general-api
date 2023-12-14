import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.exceptions.EntityNotFoundException import EntityNotFoundException
from app.models.application import Application
from app.models.channel import Channel
from app.repositories import application as application_repository
from app.repositories import channel as channel_repository
from app.repositories.channel import get_by_name
from app.schemas.account import AccountPrincipal
from app.schemas.channel import ChannelCreate, ChannelCreateResponse, ChannelListRes


async def create_channel(dto: ChannelCreate, account: AccountPrincipal, db: Session):
    application = application_repository.get_by_id(db, dto.application_id)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    new_channel = Channel(
        application_id=dto.application_id,
        uuid=uuid.uuid4(),
        name=dto.name,
        max_members=100,
        created_by=account.email,
        updated_by=account.email,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    new_channel_response = ChannelCreateResponse(
        uuid=new_channel.uuid,
        id=new_channel.id,
        name=new_channel.name,
        application_id=new_channel.application_id,
        max_members=new_channel.max_members,
        created_at=new_channel.created_at,
        updated_at=new_channel.updated_at,
    )
    return new_channel_response


async def view_channel(db: Session, name: str):
    if not get_by_name(db, name):
        return {"error": "the channel does not exist"}

    return get_by_name(db, name)


async def list_channel(
    application_id: int, search_keyword: str, account: AccountPrincipal, db: Session
):
    application = application_repository.get_by_id(db, application_id)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    channels_with_user_cnt = channel_repository.list_channels_with_user_count(
        application_id, search_keyword, db
    )
    channel_ids_with_last_message_at = (
        channel_repository.list_channel_ids_with_last_message_at(
            application_id, search_keyword, db
        )
    )
    last_msg_at_per_channel = {
        channel_id: last_message_at
        for channel_id, last_message_at in channel_ids_with_last_message_at
    }

    return [
        ChannelListRes(
            name=channel.name,
            application_id=channel.application_id,
            max_members=channel.max_members,
            user_count=user_count,
            last_message_at=last_msg_at_per_channel.get(channel.id, None),
            created_at=channel.created_at,
            updated_at=channel.updated_at,
            uuid=channel.uuid,
            id=channel.id,
        )
        for channel, user_count in channels_with_user_cnt
    ]
