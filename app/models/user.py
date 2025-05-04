from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    messages_sent = relationship("Message", back_populates="sender",foreign_keys="Message.sender_id")
    messages_received = relationship("Message", back_populates="receiver", foreign_keys="Message.receiver_id")

    def __repr__(self):
        return f"<User {self.username}>"