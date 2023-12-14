from datetime import datetime

from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationCreateResponse(OrganizationBase):
    pass


class GetOrgResponse(OrganizationBase):
    id: int
    max_applications: int
    num_apps_in_org: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Organization(OrganizationBase):
    id: int
    max_applications: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
