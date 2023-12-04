from sqlalchemy.sql import func
from app.models.channel import Channel


async def create_channel(dto, db):
    new_channel = Channel(
        application_id=dto.application_id,
        name=dto.name,
        # TODO: should discuss Daniel what this Max_members value should be?
        max_members=20,
        created_at=func.now(),
        created_by="system",
        updated_at=func.now(),
        updated_by="system",
    )
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    return new_channel
