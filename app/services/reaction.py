from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.reaction import Reaction
from app.schemas.reaction import NewReaction, NewReactionResponse
from ..repositories import message as message_repository
from ..repositories import reaction as reaction_repository
from ..repositories import user as user_repository


async def new_reaction(dto: NewReaction, db: Session):
    user = user_repository.get_by_application_id_and_username(
        db, 3, dto.username
    )  # todo remove hard coded app id
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    message = message_repository.get_by_uuid(db, dto.message_uuid)
    if not message:
        raise HTTPException(status_code=400, detail="Message does not exist")

    existing_reaction = (
        reaction_repository.get_reaction_by_message_id_and_user_id_and_reaction(
            db=db,
            message_id=message.id,
            user_id=user.id,
            reaction=dto.reaction,
        )
    )
    operation = "ADD"
    if existing_reaction:
        db.delete(existing_reaction)
        operation = "DELETE"
    else:
        reaction = Reaction(
            message_id=message.id,
            reaction=dto.reaction,
            user_id=user.id,
            created_by=user.username,
            updated_by=user.username,
        )
        db.add(reaction)
    db.commit()

    return NewReactionResponse(
        reaction=dto.reaction,
        username=user.username,
        message_uuid=str(message.uuid),
        operation=operation,
    )
