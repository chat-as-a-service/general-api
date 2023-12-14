from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.api_key_auth import check_auth
from ..core.db import get_db
from ..schemas.reaction import NewReaction
from ..services import reaction as reaction_service

router = APIRouter(dependencies=[Depends(check_auth)])


@router.post("")
async def new_reaction(dto: NewReaction, db: Session = Depends(get_db)):
    return await reaction_service.new_reaction(dto, db)
