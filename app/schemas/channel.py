from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ChannelBase(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    application_id: int


class ChannelCreate(ChannelBase):
    pass


class ChannelCreateResponse(ChannelBase):
    id: int
    uuid: UUID
    max_members: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class ChannelListRes(ChannelBase):
    id: int
    uuid: UUID
    max_members: int
    user_count: int
    last_message_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Channel(ChannelBase):
    id: int
    uuid: UUID
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
