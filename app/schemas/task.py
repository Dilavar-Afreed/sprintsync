from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    status: str = "TODO"
    total_minutes: int = 0


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    total_minutes: Optional[int] = None


class TaskStatusUpdate(BaseModel):
    status: str


class TaskResponse(TaskBase):
    id: int
    status: str
    total_minutes: int
    created_at: datetime

    class Config:
        from_attributes = True