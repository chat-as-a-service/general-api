from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    nickname: str
    application_id: int


class UserCreate(UserBase):
    pass


class UserCreateResponse(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
