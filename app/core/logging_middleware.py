import time
import json
import logging
import traceback
from fastapi import Request
from app.core.metrics import metrics

logger = logging.getLogger("sprintsync")
logging.basicConfig(level=logging.INFO)


async def log_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)
        latency = round((time.time() - start_time) * 1000, 2)
        metrics.record_request(request.url.path, latency, response.status_code)

        user_id = None
        if hasattr(request.state, "user"):
            user_id = getattr(request.state.user, "id", None)

        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "user_id": user_id,
            "latency_ms": latency,
        }

        logger.info(json.dumps(log_data))
        return response

    except Exception as e:
        latency = round((time.time() - start_time) * 1000, 2)

        error_log = {
            "method": request.method,
            "path": request.url.path,
            "status_code": 500,
            "latency_ms": latency,
            "error": str(e),
            "traceback": traceback.format_exc(),
        }

        logger.error(json.dumps(error_log))
        raise