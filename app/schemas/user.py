from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    nickname: str
    application_id: int


class UserCreate(UserBase):
    pass


class UserCreateSessionTokenReq(BaseModel):
    username: str
    application_id: int


class UserCreateSessionTokenRes(BaseModel):
    session_token: str


class UserListRes(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class UserCreateResponse(UserBase):
    pass


class UserViewRes(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class UserDeleteReq(BaseModel):
    application_id: int
    deleting_usernames: List[str]


class UserDeleteRes(BaseModel):
    deleted_usernames: List[str]


class User(UserBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
