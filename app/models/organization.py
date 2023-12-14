# flake8: noqa: F821
from datetime import datetime, timezone
from typing import List

from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship, Mapped

from ..database import Base


class Organization(Base):
    __tablename__ = "organization"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    max_applications = Column(Integer, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    created_by = Column(String(255), nullable=False)
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_by = Column(String(255), nullable=False)
    accounts: Mapped[List["Account"]] = relationship(
        "Account", back_populates="organization", cascade="all, delete"
    )
    applications: Mapped[List["Application"]] = relationship(
        "Application", back_populates="organization", cascade="all, delete"
    )
