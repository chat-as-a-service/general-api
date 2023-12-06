from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import get_by_application_id_and_username, get_by_name
from app.schemas.user import UserCreate
from sqlalchemy.sql import func


async def create_user(dto: UserCreate, db):
    # in the database, it needs unique application ID and username
    if get_by_application_id_and_username(db, dto.application_id, dto.username):
        return {"error": "application_id_and_username already exists"}
    new_user = User(
        username=dto.username,
        nickname=dto.nickname,
        application_id=dto.application_id,
        created_at=func.now(),
        created_by="system",
        updated_at=func.now(),
        updated_by="system",
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def view_user(db: Session, name: str):
    if not get_by_name(db, name):
        return {"error": "the organization may not exist"}

    return get_by_name(db, name)
