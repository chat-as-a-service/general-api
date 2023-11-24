from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from ..database import Base


class ChannelUsers(Base):
    __tablename__ = "channel_users"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    channel_id = Column(BigInteger, ForeignKey("channel.py.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_by = Column(String(255), nullable=False)
