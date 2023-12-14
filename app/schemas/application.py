from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ApplicationBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    organization_id: Optional[int] = None


class ApplicationIdType(str, Enum):
    uuid = "uuid"
    id = "id"


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationEdit(ApplicationBase):
    pass


class ApplicationCreateResponse(ApplicationBase):
    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class ApplicationEditResponse(ApplicationBase):
    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class ApplicationListResponse(ApplicationBase):
    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class ApplicationViewResponse(ApplicationBase):
    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class ApplicationGetMasterApiKeyReq(BaseModel):
    password: str


class ApplicationGetMasterApiKeyRes(BaseModel):
    master_api_key: str


class Application(ApplicationBase):
    id: int
    uuid: UUID
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
