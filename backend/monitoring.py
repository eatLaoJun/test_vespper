from prometheus_client import Counter, Histogram
from flask import request, jsonify
import time  


# 定义指标
REQUEST_COUNT = Counter(
    'flask_request_count', 'App Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'flask_request_latency_seconds', 'Request latency',
    ['method', 'endpoint']
)
EXCEPTION_COUNT = Counter(
    'flask_exception_count', 'App Exception Count',
    ['method', 'endpoint', 'exception_type']
)

def start_monitoring(app):
    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def after_request(response):
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            http_status=response.status_code
        ).inc()
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.path
        ).observe(time.time() - request.start_time)
        return response

    @app.errorhandler(Exception)
    def handle_exception(error):
        EXCEPTION_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            exception_type=type(error).__name__
        ).inc()
        # 这里可以添加您原有的异常处理逻辑
        return jsonify({"error": "Internal Server Error"}), 500