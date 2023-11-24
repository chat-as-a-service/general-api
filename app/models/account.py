from datetime import datetime, timezone

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP, TEXT

from .organization import Organization
from ..database import Base


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
