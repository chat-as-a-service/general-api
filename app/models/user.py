# flake8: noqa: F821
from typing import List

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship, Mapped

from ..database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True)
    application_id = Column(BigInteger, ForeignKey("application.id"), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    nickname = Column(String(255), nullable=False)
    moderator_account_id = Column(BigInteger, ForeignKey("account.id"), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
    application = relationship("Application", back_populates="users")
    channels: Mapped[List["Channel"]] = relationship(
        "Channel", secondary="channel_users", back_populates="users"
    )
    moderator_account = relationship("Account", back_populates="moderator_user")
