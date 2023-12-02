from sqlalchemy.orm import Session

from app.core.hashing import Hasher
from app.models.account import Account
from app.repositories.account import get_by_email
from app.schemas.account import AccountCreate


async def create_account(dto: AccountCreate, db: Session):
    if get_by_email(db, dto.email):
        return {"error": "email already exists"}
    hashed_pw = Hasher.get_password_hash(dto.password)
    new_account = Account(
        email=dto.email,
        password=hashed_pw,
        first_name=dto.first_name,
        last_name=dto.last_name,
        organization_id=None,
        created_by="system",
        updated_by="system",
    )
    db.add(new_account)
    db.commit()

    return f"{new_account.email} created successfully"
