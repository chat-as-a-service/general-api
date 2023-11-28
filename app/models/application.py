from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from ..database import Base


class Application(Base):
    __tablename__ = "application"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    organization_id = Column(BigInteger, ForeignKey("organization.id"), nullable=False)
    master_api_token = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
