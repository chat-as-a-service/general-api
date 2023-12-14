from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.channel import ChannelCreate
from ..schemas.core import AuthRequest
from ..services import channel as channel_service

router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def create_channel(
    dto: ChannelCreate, request: AuthRequest, db: Session = Depends(get_db)
):
    return await channel_service.create_channel(dto, request.account, db)


@router.get("/{channelName}")
async def view_channel(channelName: str, db: Session = Depends(get_db)):
    return await channel_service.view_channel(db, channelName)


@router.get("")
async def list_channel(
    application_id: int,
    request: AuthRequest,
    search_keyword="",
    db: Session = Depends(get_db),
):
    return await channel_service.list_channel(
        application_id, search_keyword, request.account, db
    )
