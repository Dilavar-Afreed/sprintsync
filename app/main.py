from fastapi import FastAPI
from app.db.session import engine
from sqlalchemy import text

app = FastAPI(
    title="SprintSync API",
    version="0.1.0",
    description="Internal sprint tracking tool for AI consultancy"
)


@app.on_event("startup")
def test_db_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Database connected successfully ✅")


@app.get("/health")
def health_check():
    return {"status": "healthy"}