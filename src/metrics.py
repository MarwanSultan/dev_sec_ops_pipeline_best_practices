# src/metrics.py
from prometheus_client import start_http_server, Counter, Gauge

# Start metrics HTTP server
# Exposes metrics at http://localhost:8000/metrics
start_http_server(8000)

# Metrics definitions
test_runs_total = Counter('test_runs_total', 'Total number of test runs')
test_failures_total = Counter('test_failures_total', 'Total number of test failures')
test_duration_seconds = Gauge('test_duration_seconds', 'Duration of each test in seconds')
