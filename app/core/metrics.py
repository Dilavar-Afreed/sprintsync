from collections import defaultdict
from threading import Lock

class Metrics:
    def __init__(self):
        self.total_requests = 0
        self.error_count = 0
        self.total_latency = 0.0
        self.requests_by_path = defaultdict(int)
        self.lock = Lock()

    def record_request(self, path: str, latency_ms: float, status_code: int):
        with self.lock:
            self.total_requests += 1
            self.total_latency += latency_ms
            self.requests_by_path[path] += 1

            if status_code >= 400:
                self.error_count += 1

    def get_metrics(self):
        avg_latency = (
            self.total_latency / self.total_requests
            if self.total_requests > 0
            else 0
        )

        return {
            "total_requests": self.total_requests,
            "error_count": self.error_count,
            "average_latency_ms": round(avg_latency, 2),
            "requests_by_path": dict(self.requests_by_path),
        }


metrics = Metrics()