from datetime import datetime, timezone

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP, TEXT
from sqlalchemy.orm import relationship, Mapped

from app.core import log
from .organization import Organization
from ..database import Base

log = log.getLogger(__name__)


class Account(Base):
    __tablename__ = "account"
    id = Column(BigInteger, primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(TEXT, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
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
        "Organization", back_populates="accounts"
    )
    moderator_user = relationship("User", back_populates="moderator_account")
