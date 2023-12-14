from sqlalchemy.orm import Session, joinedload

from app.models.account import Account


def get_by_email(db: Session, email: str):
    return db.query(Account).filter(Account.email == email).first()


def get_by_email_with_org(email: str, db: Session):
    return (
        db.query(Account)
        .options(joinedload(Account.organization))
        .filter(Account.email == email)
        .first()
    )


def get_by_api_token(db: Session, api_token: str):
    return db.query(Account).filter(Account.api_token == api_token).first()
