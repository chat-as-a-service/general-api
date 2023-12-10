from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer, text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID

from .application import Application
from ..database import Base


class Channel(Base):
    __tablename__ = "channel"
    id = Column(BigInteger, primary_key=True)
    uuid = Column(
        UUID, nullable=False, unique=True, server_default=text("gen_random_uuid()")
    )
    name = Column(String(255), nullable=False)
    max_members = Column(Integer, nullable=False)
    application_id = Column(BigInteger, ForeignKey(Application.id), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
