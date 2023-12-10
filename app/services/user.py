from datetime import datetime, timezone

from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import (
    get_by_application_id_and_username,
    get_by_name,
    get_all_user_list,
)
from app.schemas.user import UserCreate, UserCreateResponse


async def create_user(dto: UserCreate, db):
    # in the database, it needs unique application ID and username
    if get_by_application_id_and_username(db, dto.application_id, dto.username):
        return {"error": "application_id_and_username already exists"}
    new_user = User(
        username=dto.username,
        nickname=dto.nickname,
        application_id=dto.application_id,
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


async def view_user(db: Session, name: str):
    if not get_by_name(db, name):
        return {"error": "the user may not exist"}

    return get_by_name(db, name)


async def list_users(db: Session):
    users = get_all_user_list(db)

    return users
