from datetime import datetime, timezone, timedelta
from typing import List

import jwt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.exceptions.EntityNotFoundException import EntityNotFoundException
from app.models.application import Application
from app.models.user import User
from app.repositories import application as application_repository
from app.repositories import user as user_repository
from app.repositories.user import (
    get_by_application_id_and_username,
    get_by_username,
    get_all_users_in_app,
)
from app.schemas.account import AccountPrincipal
from app.schemas.user import (
    UserCreate,
    UserCreateResponse,
    UserListRes,
    UserViewRes,
    UserDeleteReq,
    UserDeleteRes,
    UserCreateSessionTokenReq,
    UserCreateSessionTokenRes,
)


async def create_user(
    dto: UserCreate, account: AccountPrincipal, db: Session
) -> UserCreateResponse:
    application = application_repository.get_by_id(db, dto.application_id)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    if get_by_application_id_and_username(db, dto.application_id, dto.username):
        raise HTTPException(
            status_code=400, detail="User with same username already exists"
        )
    new_user = User(
        username=dto.username,
        nickname=dto.nickname,
        application_id=application.id,
        created_by="system",
        updated_by="system",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_user_response = UserCreateResponse(
        username=new_user.username,
        nickname=new_user.nickname,
        application_id=new_user.application_id,
    )
    return new_user_response


async def create_user_session_token(
    dto: UserCreateSessionTokenReq, account: AccountPrincipal, db: Session
) -> UserCreateSessionTokenRes:
    application = application_repository.get_by_id(db, dto.application_id)
    if not application:
        raise EntityNotFoundException(Application)

    user = get_by_application_id_and_username(db, dto.application_id, dto.username)
    if not user:
        raise EntityNotFoundException(User)

    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    algo = "HS256"
    payload = {
        "sub": f"{user.username}@{application.uuid}",
        "exp": datetime.now(timezone.utc) + timedelta(hours=8),
        "iss": "wingflo",
        "iat": datetime.now(timezone.utc),
        "username": user.username,
        "application_uuid": str(application.uuid),
    }
    token = jwt.encode(
        payload=payload, key=application.master_api_token, algorithm=algo
    )
    return UserCreateSessionTokenRes(session_token=token)


async def view_user(
    username: str, application_id: int, account: AccountPrincipal, db: Session
):
    application = application_repository.get_by_id(db, application_id)
    if not application:
        raise HTTPException(
            status_code=400, detail=f"Application {application_id} not found"
        )
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    user = get_by_username(db, username)

    if not user:
        raise EntityNotFoundException(User)

    return UserViewRes(
        id=user.id,
        username=user.username,
        nickname=user.nickname,
        application_id=user.application_id,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


async def list_users(
    account: AccountPrincipal, application_id: int, search_keyword: str, db: Session
) -> List[UserListRes]:
    application = application_repository.get_by_id(db, application_id)
    if not application:
        raise HTTPException(
            status_code=400, detail=f"Application {application_id} not found"
        )
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    users = get_all_users_in_app(application_id, search_keyword, db)

    return list(
        map(
            lambda user: UserListRes(
                id=user.id,
                username=user.username,
                nickname=user.nickname,
                application_id=user.application_id,
                created_at=user.created_at,
                updated_at=user.updated_at,
            ),
            users,
        )
    )


async def delete_users(dto: UserDeleteReq, account: AccountPrincipal, db: Session):
    application = application_repository.get_by_id(db, dto.application_id)
    if not application:
        raise HTTPException(
            status_code=400, detail=f"Application {dto.application_id} not found"
        )
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    deleted_usernames = user_repository.delete_users(
        dto.application_id, dto.deleting_usernames, db
    )
    db.commit()
    return UserDeleteRes(deleted_usernames=deleted_usernames)
