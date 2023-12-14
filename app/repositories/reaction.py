from sqlalchemy.orm import Session

from app.models.reaction import Reaction


def get_reaction_by_message_id_and_user_id_and_reaction(
    db: Session, message_id: int, user_id: int, reaction: str
):
    return (
        db.query(Reaction)
        .filter(
            Reaction.message_id == message_id,
            Reaction.user_id == user_id,
            Reaction.reaction == reaction,
        )
        .first()
    )
