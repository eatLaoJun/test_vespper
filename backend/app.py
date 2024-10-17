from flask import Flask, jsonify

app = Flask(__name__, static_folder='frontend')

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
        return jsonify({"message": "此接口可以正常访问"}), 200
    except Exception as e:
        # 如果捕获到异常，返回错误响应
        return jsonify({"error": "内部服务器错误", "details": str(e)}), 500

@app.route('/')
def root_endpoint():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9991)