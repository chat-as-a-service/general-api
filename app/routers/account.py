from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.account import AccountCreate
from ..services import account as account_service

router = APIRouter()


@router.post("/")
async def create_account(dto: AccountCreate, db: Session = Depends(get_db)):
    return await account_service.create_account(dto, db)
