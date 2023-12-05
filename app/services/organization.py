from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.repositories.organization import get_by_id, get_by_name
from app.schemas.organization import OrganizationCreate, OrganizationCreateResponse


async def organization_create(dto: OrganizationCreate, db: Session):
    if get_by_name(db, dto.name):
        return {"error": "organization already exists"}

    new_organization = Organization(
        name=dto.name,
        created_by="system",
        updated_by="system",
    )
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    new_organization_response = OrganizationCreateResponse(name=dto.name)
    return new_organization_response


async def organization_view(db: Session, ID: int):
    if not get_by_id(db, ID):
        return {"error": "the organization may not exist"}

    return get_by_id(db, ID)
