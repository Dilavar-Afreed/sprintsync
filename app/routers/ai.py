from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.core.security import get_current_user
from app.services.ai_service import generate_daily_plan

router = APIRouter(prefix="/ai", tags=["AI"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/suggest")
def suggest_daily_plan(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()

    return generate_daily_plan(tasks)