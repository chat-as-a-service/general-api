from datetime import datetime

from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationCreateResponse(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str
    account: str

    class Config:
        orm_mode = True
