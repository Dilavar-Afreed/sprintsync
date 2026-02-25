from fastapi import FastAPI
from app.db.session import engine
from sqlalchemy import text
from app.db.session import Base
from app.models import user  # Important import
from app.routers import auth
from app.core.security import get_current_user
from app.models.user import User
from fastapi import Depends
from app.models import task
from app.routers import tasks
from app.routers import ai
from app.core.logging_middleware import log_requests
from app.routers import metrics
from app.routers import stats

app = FastAPI(
    title="SprintSync API",
    version="0.1.0",
    description="Internal sprint tracking tool for AI consultancy"
)
app.middleware("http")(log_requests)
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(ai.router)
app.include_router(metrics.router)
app.include_router(stats.router)


@app.on_event("startup")
def startup():
    # Test connection
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Database connected successfully ✅")

    # Create tables
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully ✅")


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_admin": current_user.is_admin,
    }