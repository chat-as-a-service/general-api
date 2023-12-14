from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.core import AuthRequest
from ..schemas.organization import OrganizationCreate
from ..services import organization as organization_service

router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def organization_creation(
    dto: OrganizationCreate, request: AuthRequest, db: Session = Depends(get_db)
):
    return await organization_service.organization_create(dto, request.account, db)


@router.get("/{organization_id}")
async def organization_view(organization_id: int, db: Session = Depends(get_db)):
    return await organization_service.organization_view(db, organization_id)
