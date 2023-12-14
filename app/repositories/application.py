# flake8: noqa: F821
from typing import cast

from sqlalchemy.orm import Session

from app.models.application import Application


def get_by_api_token(db: Session, api_token: str):
    return (
        db.query(Application).filter(Application.master_api_token == api_token).first()
    )


def get_by_name(db: Session, name: str):
    return db.query(Application).filter(Application.name == name).first()


def search_by_name(db: Session, name: str, organization_id: int):
    return (
        db.query(Application)
        .filter(
            cast("ColumnElement[bool]", Application.organization_id == organization_id),
            cast("ColumnElement[bool]", Application.name.like(f"{name}%")),
        )
        .first()
    )


def get_by_id(db: Session, app_id: int) -> Application | None:
    return db.query(Application).filter(Application.id == app_id).first()


def get_by_uuid(db: Session, app_uuid: str):
    return db.query(Application).filter(Application.uuid == app_uuid).first()


def list_applications(organization_id: int, search_keyword: str | None, db: Session):
    query = db.query(Application).filter(
        cast("ColumnElement[bool]", Application.organization_id == organization_id)
    )
    if search_keyword and search_keyword.strip() != "":
        query = query.filter(
            cast("ColumnElement[bool]", Application.name.like(f"{search_keyword}%"))
        )
    return query.order_by(Application.created_at).all()


def count_apps_in_org(org_id: int, db: Session):
    return db.query(Application).filter(Application.organization_id == org_id).count()
