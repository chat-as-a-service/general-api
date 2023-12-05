from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.application import ApplicationCreate
from ..services import application as application_service
from ..core.api_key_auth import check_access_token

router = APIRouter(dependencies=[Depends(check_access_token)])


@router.post("/")
async def application_create(dto: ApplicationCreate, db: Session = Depends(get_db)):
    return await application_service.application_create(dto, db)


@router.get("/{applicationID}")
async def application_view(applicationID: int, db: Session = Depends(get_db)):
    return await application_service.application_view(applicationID, db)


@router.get("/")
async def application_list(db: Session = Depends(get_db)):
    return await application_service.application_list(db)
