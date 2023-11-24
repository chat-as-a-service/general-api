from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from ..database import Base


class Message(Base):
    __tablename__ = "message"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    channel_id = Column(BigInteger, ForeignKey("channel.id"), nullable=False)
    message = Column(String(3000), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
