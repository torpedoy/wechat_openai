# 基于Python 3.8镜像
FROM python:3.8

# 安装Redis客户端和相关依赖
RUN apt-get update && apt-get install -y redis-tools

# 安装Python依赖
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# 将应用程序复制到容器中
COPY run.py /app/

# 设置工作目录
WORKDIR /app

# 启动应用程序
CMD ["python", "run.py"]