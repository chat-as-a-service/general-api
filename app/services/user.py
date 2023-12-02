from sqlalchemy.orm import Session

from app.core.hashing import Hasher
from app.models.account import Account
from app.repositories.account import get_by_id
from app.schemas.account import AccountCreate

async def create_user(dto, db):
    if get_by_id(db, dto.id):
        return {"error": "id already exists"}
    new_user = Account(
        id=dto.id,
        username=dto.username,
        nickname=dto.nickname,
        application_id=dto.application_id,
        created_by="system",
        updated_by="system",
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user