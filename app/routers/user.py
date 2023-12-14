from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.core import AuthRequest
from ..schemas.user import UserCreate, UserDeleteReq, UserCreateSessionTokenReq
from ..services import user as user_service

router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def create_user(
    dto: UserCreate, request: AuthRequest, db: Session = Depends(get_db)
):
    return await user_service.create_user(dto, request.account, db)


@router.post("/session-token")
async def create_session_token(
    dto: UserCreateSessionTokenReq, request: AuthRequest, db: Session = Depends(get_db)
):
    return await user_service.create_user_session_token(dto, request.account, db)


@router.get("/{username}")
async def view_user(
    username: str,
    application_id: int,
    request: AuthRequest,
    db: Session = Depends(get_db),
):
    return await user_service.view_user(username, application_id, request.account, db)


@router.get("")
async def list_users(
    request: AuthRequest,
    application_id: int,
    search_keyword: str = "",
    db: Session = Depends(get_db),
):
    return await user_service.list_users(
        request.account, application_id, search_keyword, db
    )


@router.delete("")
async def delete_users(
    request: AuthRequest,
    dto: UserDeleteReq,
    db: Session = Depends(get_db),
):
    return await user_service.delete_users(dto, request.account, db)
