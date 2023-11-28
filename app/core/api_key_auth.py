from fastapi import Security, HTTPException, Depends
from fastapi.security import api_key
from sqlalchemy.orm import Session

from app.core import log
from app.core.db import get_db
from ..services import application as application_service

log = log.getLogger(__name__)
api_key_header = api_key.APIKeyHeader(name="Api-Token")


async def check_api_token(api_token: str = Security(api_key_header), db: Session = Depends(get_db)):
    log.info("Checking Api-Token header")
    api_key_valid = await application_service.check_api_token(api_token, db)
    if not api_key_valid:
        raise HTTPException(
            status_code=401, detail="Unauthorized - API Key is wrong"
        )
    return None
