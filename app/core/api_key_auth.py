from fastapi import Security, HTTPException, Depends
from fastapi.security import api_key, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core import log
from app.core.db import get_db
from ..services import application as application_service


import jwt
import os

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


def check_access_token(token: str = Depends(access_token)):
    credentials_exception = HTTPException(
        status_code=401, detail="Unauthorized - access token verification failed"
    )

    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    return None
