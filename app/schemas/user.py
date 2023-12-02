from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    nickname: str
    first_name: str
    last_name: str
    application_id: int

class UserCreate(UserBase):
    pass

class User(UserBase):  
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True