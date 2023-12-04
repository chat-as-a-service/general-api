from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AccountBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    organization_id: Optional[int] = None


class UserBase(BaseModel):
    username: str
    nickname: str
    first_name: str
    last_name: str
    application_id: int


class AccountSignin(BaseModel):
    email: EmailStr
    password: str


class AccountCreate(AccountBase):
    password: str


class AccountCreateResponse(AccountBase):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):  # UserBase를 상속받음
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True


class Account(AccountBase):
    id: int
    password: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
