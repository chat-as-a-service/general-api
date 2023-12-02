from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.account import AccountCreate, AccountSignin
from ..services import account as account_service
from app.core.api_key_auth import check_api_token

router = APIRouter()
secured_router = APIRouter(dependencies=[Depends(check_api_token)])


@router.post("/")
async def create_account(dto: AccountCreate, db: Session = Depends(get_db)):
    return await account_service.create_account(dto, db)


@router.post("/signin")
async def account_signin(dto: AccountSignin, db: Session = Depends(get_db)):
    return await account_service.account_signin(dto, db)
