from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.user import UserCreate
from ..services import account as account_service

router = APIRouter()


@router.post("/")
async def create_user(dto: UserCreate, db: Session = Depends(get_db)):
    return await account_service.create_user(dto, db)

# Compare this snippet from app/routers/user.py:
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

