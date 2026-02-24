from fastapi import FastAPI
from app.db.session import engine
from sqlalchemy import text
from app.db.session import Base
from app.models import user  # Important import
from app.routers import auth


app = FastAPI(
    title="SprintSync API",
    version="0.1.0",
    description="Internal sprint tracking tool for AI consultancy"
)
app.include_router(auth.router)


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