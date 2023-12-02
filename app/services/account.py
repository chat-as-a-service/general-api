from sqlalchemy.orm import Session

from app.core.hashing import Hasher
from app.models.account import Account
from app.repositories.account import get_by_email
from app.schemas.account import AccountCreate, AccountCreateResponse, AccountSignin
import jwt
from datetime import datetime, timedelta
import os


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
    new_account_response = AccountCreateResponse(
        email=dto.email,
        first_name=dto.first_name,
        last_name=dto.last_name,
        organization_id=None,
    )
    db.add(new_account)
    db.commit()

    return new_account_response


async def account_signin(dto: AccountSignin, db: Session):
    account = get_by_email(db, dto.email)
    if not account:
        return {"error": "the account does not exist"}

    if not Hasher.verify_password(dto.password, account.password):
        return {"error": "wrong password"}

    secret_key = os.getenv("SECRET_KEY")
    algo = "HS256"
    payload = {
        "sub": account.email,
        "exp": datetime.now() + timedelta(hours=8),
        "iss": "CaaS",
        "iat": datetime.now(),
    }

    # Generate the token
    token = jwt.encode(payload, secret_key, algorithm=algo)
    return {"token": token}
