from sqlalchemy.orm import Session

from app.models.application import Application


async def check_api_token(api_token: str, db: Session):
    application = db.query(Application).filter(Application.master_api_token == api_token).first()
    if not application:
        return False
    return True
