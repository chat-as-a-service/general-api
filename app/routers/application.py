from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.application import (
    ApplicationCreate,
    ApplicationEdit,
    ApplicationIdType,
    ApplicationGetMasterApiKeyReq,
)
from ..schemas.core import AuthRequest
from ..services import application as application_service

router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def application_create(
    dto: ApplicationCreate, request: AuthRequest, db: Session = Depends(get_db)
):
    return await application_service.application_create(dto, request.account, db)


@router.put("/{application_id}")
async def application_edit(
    dto: ApplicationEdit,
    application_id: int,
    request: AuthRequest,
    db: Session = Depends(get_db),
):
    return await application_service.application_edit(
        dto, application_id, request.email, db
    )


@router.delete("/{application_id}")
async def application_delete(
    application_id: int,
    request: AuthRequest,
    db: Session = Depends(get_db),
):
    return await application_service.application_delete(
        application_id, request.email, db
    )


@router.get("/{application_id_or_uuid}")
async def application_view(
    application_id_or_uuid: str,
    id_type: ApplicationIdType,
    request: AuthRequest,
    db: Session = Depends(get_db),
):
    return await application_service.application_view(
        application_id_or_uuid, id_type, request.email, db
    )


@router.get("")
async def application_list(
    request: AuthRequest,
    search_keyword: str | None = None,
    db: Session = Depends(get_db),
):
    return await application_service.application_list(
        request.account, search_keyword, db
    )


@router.post("/{application_id}/master-api-key")
async def get_master_api_key(
    request: AuthRequest,
    application_id: int,
    dto: ApplicationGetMasterApiKeyReq,
    db: Session = Depends(get_db),
):
    return await application_service.get_master_api_key(
        application_id, request.account, dto.password, db
    )
