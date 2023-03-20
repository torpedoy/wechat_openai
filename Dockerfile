# 基于Python 3.8镜像
FROM python:3.8-slim

# 安装Redis客户端和相关依赖
RUN apt-get update && apt-get install -y redis-server

# 安装Python依赖
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# 设置工作目录
WORKDIR /app

# 启动应用程序
CMD ["python", "run.py"]