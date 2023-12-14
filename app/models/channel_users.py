from sqlalchemy import Column, BigInteger, String, ForeignKey, Table
from sqlalchemy.dialects.postgresql import TIMESTAMP

from ..database import Base

# class ChannelUsers(Base):
#     __tablename__ = "channel_users"
#     id = Column(BigInteger, primary_key=True)
#     user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
#     channel_id = Column(BigInteger, ForeignKey("channel.py.id"), nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False)
#     created_by = Column(String(255), nullable=False)
#     updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
#     updated_by = Column(String(255), nullable=False)


channel_users = Table(
    "channel_users",
    Base.metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("user.id"), nullable=False),
    Column("channel_id", BigInteger, ForeignKey("channel.id"), nullable=False),
    Column("created_at", TIMESTAMP(timezone=True), nullable=False),
    Column("created_by", String(255), nullable=False),
    Column("updated_at", TIMESTAMP(timezone=True), nullable=False),
    Column("updated_by", String(255), nullable=False),
)
