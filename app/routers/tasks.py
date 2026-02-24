from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    TaskStatusUpdate,
)
from app.core.security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🟢 Create Task
@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# 🟢 Get All Tasks (Only Current User's)
@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks


# 🟢 Get Single Task
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# 🟢 Update Task
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


# 🟢 Update Status Only
@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_status(
    task_id: int,
    status_update: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = status_update.status

    db.commit()
    db.refresh(task)

    return task


# 🟢 Delete Task
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"detail": "Task deleted successfully"}