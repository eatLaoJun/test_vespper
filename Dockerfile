# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制后端代码
COPY app.py .

# 暴露端口
EXPOSE 5000

# 设置容器启动时运行的命令
CMD ["python", "app.py"]