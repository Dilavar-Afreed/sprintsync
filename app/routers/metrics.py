from fastapi import APIRouter
from app.core.metrics import metrics

router = APIRouter(tags=["Metrics"])

@router.get("/metrics")
def get_metrics():
    return metrics.get_metrics()