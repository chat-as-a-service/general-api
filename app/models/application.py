# flake8: noqa: F821
import secrets
from datetime import datetime, timezone
from typing import List

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, relationship

from .organization import Organization
from ..database import Base


class Application(Base):
    __tablename__ = "application"
    id = Column(BigInteger, primary_key=True)
    uuid = Column(UUID, nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    master_api_token = Column(
        String(255), nullable=False, default=secrets.token_urlsafe(32)
    )
    organization_id = Column(BigInteger, ForeignKey(Organization.id), nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    created_by = Column(String(255), nullable=False)
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_by = Column(String(255), nullable=False)

    organization: Mapped["Organization"] = relationship(
        "Organization", back_populates="applications"
    )

    channels: Mapped[List["Channel"]] = relationship(
        "Channel", back_populates="application"
    )

    users: Mapped[List["User"]] = relationship("User")
