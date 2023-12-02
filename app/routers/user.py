from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.account import UserCreate
from ..services import account as account_service

router = APIRouter()


@router.post("/")
async def create_user(dto: UserCreate, db: Session = Depends(get_db)):
    return await account_service.create_user(dto, db)

# 유저를 만들고 - 데이터베이스에 저장하고 -

홍 내가 생각하는게 맞는지 확인 좀 해줘

유저를 만들고 - 데이터베이스에 저장하고 
