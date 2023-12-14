from datetime import datetime, timezone

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP

from .message import Message
from .user import User
from ..database import Base


class Reaction(Base):
    __tablename__ = "reaction"
    id = Column(BigInteger, primary_key=True)
    reaction = Column(String(30), nullable=False)
    user_id = Column(BigInteger, ForeignKey(User.id), nullable=False)
    message_id = Column(BigInteger, ForeignKey(Message.id), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    created_by = Column(String(255), nullable=False)
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_by = Column(String(255), nullable=False)
