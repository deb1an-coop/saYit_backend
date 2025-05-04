from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    chatroom_id = Column(Integer, ForeignKey("chatrooms.id"), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Define relationships
    sender = relationship("User", back_populates="messages_sent", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="messages_received", foreign_keys=[receiver_id])
    chatroom = relationship("Chatroom", back_populates="messages")
    
    def __repr__(self):
        return f"<Message {self.id}>"