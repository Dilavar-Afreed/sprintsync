from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base
from pgvector.sqlalchemy import Vector


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="TODO")
    total_minutes = Column(Integer, default=0)

    # Original creator
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Auto-assigned user
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    embedding = Column(Vector(1536), nullable=True)

    owner = relationship(
        "User",
        back_populates="tasks",
        foreign_keys=[user_id]
    )

    assigned_user = relationship(
        "User",
        foreign_keys=[assigned_user_id]
    )