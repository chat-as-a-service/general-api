from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from ..database import Base
from datetime import datetime, timezone
from .organization import Organization
import secrets


class Application(Base):
    __tablename__ = "application"
    id = Column(BigInteger, primary_key=True)
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
