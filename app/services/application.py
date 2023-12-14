import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core import log
from app.models.application import Application
from app.repositories import organization as organization_repository
from app.repositories.account import get_by_api_token
from app.repositories.application import list_applications, get_by_id
from app.schemas.application import (
    ApplicationCreate,
    ApplicationCreateResponse,
    ApplicationListResponse,
    ApplicationEdit,
    ApplicationViewResponse,
    ApplicationIdType,
    ApplicationGetMasterApiKeyRes,
)
from ..core.hashing import Hasher
from ..exceptions.EntityNotFoundException import EntityNotFoundException
from ..models.account import Account
from ..models.organization import Organization
from ..repositories import account as account_repository
from ..repositories import application as application_repository
from ..schemas.account import AccountPrincipal

log = log.getLogger(__name__)


async def check_api_token(api_token: str, db: Session):
    application = get_by_api_token(db, api_token)
    if not application:
        return False
    return True


async def application_create(
    dto: ApplicationCreate, account: AccountPrincipal, db: Session
):
    org = organization_repository.get_by_id(db, account.organization_id)
    if not org:
        log.error(f"Organization with id {account.organization_id} not found")
        raise EntityNotFoundException(Organization)

    num_apps_in_org = application_repository.count_apps_in_org(
        account.organization_id, db
    )

    if num_apps_in_org >= org.max_applications:
        log.info(
            "Max number of applications reached for organization with id {account.organization_id}"
        )
        raise HTTPException(
            status_code=400,
            detail=f"Max number of applications reached for organization {account.organization.name}",
        )

    new_application = Application(
        name=dto.name,
        uuid=uuid.uuid4(),
        organization_id=account.organization_id,
        created_by=account.email,
        updated_by=account.email,
    )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    new_application_response = ApplicationCreateResponse(
        id=new_application.id,
        uuid=new_application.uuid,
        name=new_application.name,
        created_at=new_application.created_at,
        updated_at=new_application.updated_at,
        organization_id=new_application.organization_id,
    )
    return new_application_response


async def application_edit(
    dto: ApplicationEdit, application_id: int, account_email: str, db: Session
):
    account = account_repository.get_by_email(db, account_email)
    if not account:
        raise EntityNotFoundException(Account)

    application = get_by_id(db, application_id)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    application.name = dto.name
    db.commit()
    db.refresh(application)
    application_edit_response = ApplicationCreateResponse(
        id=application.id,
        uuid=application.uuid,
        name=application.name,
        created_at=application.created_at,
        updated_at=application.updated_at,
        organization_id=application.organization_id,
    )
    return application_edit_response


async def application_delete(application_id: int, account_email: str, db: Session):
    account = account_repository.get_by_email(db, account_email)
    if not account:
        raise EntityNotFoundException(Account)

    application = get_by_id(db, application_id)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db.delete(application)
    db.commit()


async def application_view(
    application_id_or_uuid: str,
    id_type: ApplicationIdType,
    account_email: str,
    db: Session,
):
    account = account_repository.get_by_email(db, account_email)
    if id_type == ApplicationIdType.id:
        application = application_repository.get_by_id(db, int(application_id_or_uuid))
    elif id_type == ApplicationIdType.uuid:
        application = application_repository.get_by_uuid(db, application_id_or_uuid)
    else:
        raise HTTPException(status_code=400, detail="Invalid id_type")

    if not account:
        raise EntityNotFoundException(Account)
    if not application:
        raise EntityNotFoundException(Application)
    if application.organization_id != account.organization_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    return ApplicationViewResponse(
        id=application.id,
        uuid=application.uuid,
        name=application.name,
        organization_id=application.organization_id,
        created_at=application.created_at,
        updated_at=application.updated_at,
    )


async def application_list(
    account: AccountPrincipal, search_keyword: str | None, db: Session
):
    account = account_repository.get_by_email(db, account.email)
    if not account:
        raise EntityNotFoundException(Account)

    applications = list_applications(account.organization_id, search_keyword, db)
    return list(
        map(
            lambda application: ApplicationListResponse(
                id=application.id,
                uuid=application.uuid,
                name=application.name,
                organization_id=application.organization_id,
                created_at=application.created_at,
                updated_at=application.updated_at,
            ),
            applications,
        )
    )


async def get_master_api_key(
    application_id: int, account: AccountPrincipal, account_password: str, db: Session
):
    application = application_repository.get_by_id(db, application_id)
    if not application:
        raise EntityNotFoundException(Application)
    account_entity = account_repository.get_by_email(db, account.email)
    if not account_entity:
        raise EntityNotFoundException(Account)

    if Hasher.verify_password(account_password, account_entity.password):
        return ApplicationGetMasterApiKeyRes(
            master_api_key=application.master_api_token
        )
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
