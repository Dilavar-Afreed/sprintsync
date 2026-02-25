from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import SessionLocal
from app.models.user import User
from app.models.task import Task

router = APIRouter(prefix="/stats", tags=["Stats"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/top-users")
def top_users(db: Session = Depends(get_db)):
    results = (
        db.query(
            User.id,
            User.email,
            func.sum(Task.total_minutes).label("total_minutes")
        )
        .join(Task, Task.assigned_user_id == User.id)
        .group_by(User.id)
        .order_by(func.sum(Task.total_minutes).desc())
        .limit(5)
        .all()
    )

    return {
        "top_users": [
            {
                "user_id": r.id,
                "email": r.email,
                "total_minutes": r.total_minutes or 0
            }
            for r in results
        ]
    }