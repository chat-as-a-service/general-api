from sqlalchemy.orm import Session

from app.repositories.account import get_by_api_token


async def check_api_token(api_token: str, db: Session):
    application = get_by_api_token(db, api_token)
    if not application:
        return False
    return True
