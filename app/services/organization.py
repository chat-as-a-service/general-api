from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.repositories import account as account_repository
from app.repositories import application as application_repository
from app.repositories.organization import get_by_id, get_by_name
from app.schemas.account import AccountPrincipal
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationCreateResponse,
    GetOrgResponse,
)


async def organization_create(
    dto: OrganizationCreate, account: AccountPrincipal, db: Session
):
    if get_by_name(db, dto.name):
        return {"error": "organization already exists"}

    new_organization = Organization(
        name=dto.name,
        max_applications=10,
        created_by="system",
        updated_by="system",
    )
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)

    account = account_repository.get_by_email(db, account.email)
    account.organization_id = new_organization.id
    db.commit()
    db.refresh(account)
    new_organization_response = OrganizationCreateResponse(name=dto.name)
    return new_organization_response


async def organization_view(db: Session, organization_id: int):
    organization = get_by_id(db, organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    num_apps_in_org = application_repository.count_apps_in_org(organization_id, db)

    return GetOrgResponse(
        id=organization.id,
        name=organization.name,
        num_apps_in_org=num_apps_in_org,
        max_applications=organization.max_applications,
        created_at=organization.created_at,
        updated_at=organization.updated_at,
    )
