from sqlalchemy.orm import Session

from app.models.user import user

def get_by_id(db: Session, id: int):
    return db.query(user).filter(user.id == id).first()