from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AccountBase(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    organization_id: Optional[int] = None


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
