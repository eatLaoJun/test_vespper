from flask import Flask, jsonify, Response, send_from_directory
from flask_cors import CORS  # 导入 CORS
import prometheus_client
from monitoring import start_monitoring  # 导入监控模块
from prometheus_client import Counter

EXCEPTION_COUNTER = Counter('flask_exception_count', 'App Exception Count', ['endpoint', 'exception_type', 'method'])


app = Flask(__name__, static_folder='../frontend')
CORS(app)  # 启用 CORS

# 启动监控
start_monitoring(app)


@app.route('/ok', methods=['GET'])
def accessible_endpoint():
    return jsonify({"message": "此接口可以正常访问"}), 200

@app.route('/o', methods=['GET'])
def not_accessible_endpoint():
    try:
        # 模拟可能引发异常的操作
        # 这里可以放置您的业务逻辑代码
        # 例如: raise ValueError("一个示例异常")
        raise Exception("一个示例异常")
        # 如果没有异常发生，返回成功的响应
        return jsonify({"message": "此接口可以正常访问o "}), 200
    except Exception as e:
        # 如果捕获到异常，返回错误响应
        EXCEPTION_COUNTER.labels(endpoint='/o', exception_type=type(e).__name__, method='GET').inc()
        return jsonify({"error": "内部服务器错误", "details": str(e)}), 500

@app.route('/')
def root_endpoint():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/metrics')
def requests_count():
    return Response(prometheus_client.generate_latest(),mimetype="text/plain")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9991)