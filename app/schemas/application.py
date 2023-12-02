from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class ApplicationBase(BaseModel):
    name: str
    organization_id: Optional[int] = None


class ApplicationCreate(ApplicationBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
