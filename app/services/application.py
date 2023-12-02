from app.repositories.account import get_by_api_token
from sqlalchemy.orm import Session
from app.models.application import Application
from app.repositories.application import get_by_name, get_all_applications
from app.schemas.application import ApplicationCreate


async def check_api_token(api_token: str, db: Session):
    application = get_by_api_token(db, api_token)
    if not application:
        return False
    return True


async def application_create(dto: ApplicationCreate, db: Session):
    if get_by_name(db, dto.email):
        return {"error": "application name already exists"}

    new_application = Application(
        name=dto.name,
        created_by="system",
        updated_by="system",
    )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application


async def application_view(dto: ApplicationCreate, db: Session):
    if not get_by_name(db, dto.name):
        return {"error": "the name does not exist"}

    return get_by_name(db, dto.name)


async def application_list(db: Session):
    applications = get_all_applications(db)
    return applications
