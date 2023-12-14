from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.account import AccountCreate, AccountSigninReq
from ..services import account as account_service

router = APIRouter()
secured_router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def create_account(dto: AccountCreate, db: Session = Depends(get_db)):
    return await account_service.create_account(dto, db)


@router.post("/signin")
async def account_signin(dto: AccountSigninReq, db: Session = Depends(get_db)):
    return await account_service.account_signin(dto, db)


@secured_router.get("/me")
async def whoami(request: Request, db: Session = Depends(get_db)):
    return await account_service.get_user(request.email, db)
