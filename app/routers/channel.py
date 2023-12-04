from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..schemas.channel import ChannelCreate
from ..services import channel as channel_service

router = APIRouter()


@router.post("/")
async def create_user(dto: ChannelCreate, db: Session = Depends(get_db)):
    return await channel_service.create_channel(dto, db)
