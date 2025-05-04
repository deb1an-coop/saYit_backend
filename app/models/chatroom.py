from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey, func
from sqlalchemy.orm import relationship
from app.core.database import Base

# Association table for many-to-many relationship between users and chatrooms
chatroom_users = Table(
    "chatroom_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("chatroom_id", Integer, ForeignKey("chatrooms.id"))
)


class Chatroom(Base):
    __tablename__ = "chatrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Define relationships
    messages = relationship("Message", back_populates="chatroom")
    users = relationship("User", secondary=chatroom_users, backref="chatrooms")
    
    def __repr__(self):
        return f"<Chatroom {self.name}>"