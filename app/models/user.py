from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from ..database import Base
from sqlalchemy import UniqueConstraint


class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True)
    application_id = Column(BigInteger, ForeignKey("application.id"), nullable=False)
    username = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
    __table_args__ = (
        UniqueConstraint("application_id", "username", name="_application_username_uc"),
    )
