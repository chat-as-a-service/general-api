from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..schemas.account import AccountCreate
from ..services import account as account_service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_account(dto: AccountCreate, db: Session = Depends(get_db)):
    return await account_service.create_account(dto,db)
