from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.application import ApplicationCreate
from ..services import application as application_service

router = APIRouter()


@router.post("/")
async def application_create(dto: ApplicationCreate, db: Session = Depends(get_db)):
    return await application_service.application_create(dto, db)


@router.post("/view")
async def application_view(dto: ApplicationCreate, db: Session = Depends(get_db)):
    return await application_service.application_view(dto, db)


@router.post("/list")
async def application_list(db: Session = Depends(get_db)):
    return await application_service.application_list(db)
