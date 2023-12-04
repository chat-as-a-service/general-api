from sqlalchemy.orm import Session

from app.models.application import Application


def get_by_api_token(db: Session, api_token: str):
    return db.query(Application).filter(Application.master_api_token == api_token).first()
