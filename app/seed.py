from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.models.task import Task
from app.core.security import hash_password


def seed():
    db: Session = SessionLocal()
    try:
        # Check if already seeded
        if db.query(User).first():
            print("Database already seeded.")
            return

        # Create Admin User
        admin = User(
            email="admin@sprintsync.com",
            hashed_password=hash_password("admin123"),
            is_admin=True,
            resume_text="Experienced product manager with AI knowledge"
        )

        user1 = User(
            email="user1@sprintsync.com",
            hashed_password=hash_password("password123"),
            is_admin=False,
            resume_text="Backend developer with Python and FastAPI experience"
        )

        db.add_all([admin, user1])
        db.commit()
        db.refresh(admin)
        db.refresh(user1)

        # Create Tasks
        task1 = Task(
            title="Build API",
            description="Create FastAPI backend",
            user_id=admin.id
        )

        task2 = Task(
            title="Write tests",
            description="Add pytest coverage",
            user_id=user1.id
        )

        db.add_all([task1, task2])
        db.commit()

        print("Demo data inserted successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
