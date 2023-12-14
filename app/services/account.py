from datetime import datetime, timedelta, timezone

import jwt
from sqlalchemy.orm import Session

from app.core.hashing import Hasher
from app.exceptions.EntityNotFoundException import EntityNotFoundException
from app.models.account import Account
from app.repositories.account import get_by_email
from app.schemas.account import (
    AccountCreate,
    AccountCreateResponse,
    AccountSigninReq,
    AccountResponse,
    AccountSigninRes,
)
from app.settings import settings


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


async def account_signin(dto: AccountSigninReq, db: Session):
    account = get_by_email(db, dto.email)
    if not account:
        return {"error": "the account does not exist"}

    if not Hasher.verify_password(dto.password, account.password):
        return {"error": "wrong password"}

    secret_key = settings.secret_key
    algo = "HS256"
    payload = {
        "sub": account.email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=8),
        "iss": "CaaS",
        "iat": datetime.now(timezone.utc),
    }

    # Generate the token
    token = jwt.encode(payload, secret_key, algorithm=algo)
    return AccountSigninRes(token=token)


async def get_user(account_email: str, db: Session):
    account = get_by_email(db, account_email)
    if not account:
        raise EntityNotFoundException(Account)
    return AccountResponse(
        email=account.email,
        first_name=account.first_name,
        last_name=account.last_name,
        organization_id=account.organization_id,
    )
