from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AccountBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    organization_id: Optional[int] = None


class AccountSigninReq(BaseModel):
    email: EmailStr
    password: str


class AccountSigninRes(BaseModel):
    token: str


class AccountCreate(AccountBase):
    password: str


class AccountCreateResponse(AccountBase):
    pass


class AccountResponse(AccountBase):
    pass


class AccountPrincipal(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    organization_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime


class Account(AccountBase):
    id: int
    password: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
