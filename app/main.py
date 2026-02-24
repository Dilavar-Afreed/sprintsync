from fastapi import FastAPI

app = FastAPI(
    title="SprintSync API",
    version="0.1.0",
    description="Internal sprint tracking tool for AI consultancy"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}