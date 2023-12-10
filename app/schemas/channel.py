from datetime import datetime

from pydantic import BaseModel


class ChannelBase(BaseModel):
    name: str
    application_id: int


class ChannelCreate(ChannelBase):
    pass


class ChannelCreateResponse(ChannelBase):
    pass


class Channel(ChannelBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
