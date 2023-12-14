import os

import jwt
from fastapi import Security, HTTPException, Depends, Request
from fastapi.security import api_key, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core import log
from app.core.db import get_db
from ..repositories import account as account_repository
from ..schemas.account import AccountPrincipal
from ..services import application as application_service

log = log.getLogger(__name__)
api_key_header = api_key.APIKeyHeader(name="Api-Token")
access_token = OAuth2PasswordBearer(tokenUrl="token")


async def check_api_token(
    api_token: str = Security(api_key_header), db: Session = Depends(get_db)
):
    log.info("Checking Api-Token header")
    api_key_valid = await application_service.check_api_token(api_token, db)
    if not api_key_valid:
        raise HTTPException(status_code=401, detail="Unauthorized - API Key is wrong")
    return None


def check_auth(
    request: Request, token: str = Depends(access_token), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401, detail="Unauthorized - access token verification failed"
    )

    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        email: str = payload.get("sub")

        if email is None:
            log.info("Malformed token: email does not exist")
            raise credentials_exception
        else:
            account = account_repository.get_by_email(db, email)
            request.email = email
            request.account = AccountPrincipal(
                id=account.id,
                email=account.email,
                first_name=account.first_name,
                last_name=account.last_name,
                organization_id=account.organization_id,
                created_at=account.created_at,
                updated_at=account.updated_at,
            )
    except jwt.ExpiredSignatureError:
        log.info("Token expired")
        raise credentials_exception
    except jwt.InvalidTokenError:
        log.info("Invalid token")
        raise credentials_exception

    return None
