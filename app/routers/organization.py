from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.organization import OrganizationCreate
from ..services import organization as organization_service
from app.core.api_key_auth import check_api_token

router = APIRouter()
secured_router = APIRouter(dependencies=[Depends(check_api_token)])


@router.post("/")
async def organization_creation(dto: OrganizationCreate, db: Session = Depends(get_db)):
    return await organization_service.organization_create(dto, db)


@router.get("/view")
async def organization_view(dto: OrganizationCreate, db: Session = Depends(get_db)):
    return await organization_service.organization_view(dto, db)
