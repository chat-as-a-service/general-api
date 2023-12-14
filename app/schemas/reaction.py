from datetime import datetime

from pydantic import BaseModel, Field


class ReactionBase(BaseModel):
    reaction: str = Field(max_length=30)


class NewReaction(ReactionBase):
    username: str
    message_uuid: str


class NewReactionResponse(ReactionBase):
    username: str
    message_uuid: str
    operation: str


class Reaction(ReactionBase):
    id: int
    user_id: int
    message_id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
