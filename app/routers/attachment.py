from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..services import attachment as attachment_service

router = APIRouter()


@router.post("")
async def upload_attachment(file: UploadFile, db: Session = Depends(get_db)):
    return attachment_service.upload_attachment(file)
