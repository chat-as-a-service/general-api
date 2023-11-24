from typing import List

from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, relationship

from ..database import Base


class Organization(Base):
    __tablename__ = "organization"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
    accounts = relationship("Account")
