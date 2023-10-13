# 使用官方Python运行时作为基础镜像
FROM docker.nju.edu.cn/library/python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的工作目录
COPY . /app

RUN chmod +x /app/start.sh

# 安装应用程序依赖
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -i https://mirrors.aliyun.com/pypi/simple rasa


# 暴露应用程序需要的端口
EXPOSE 8000

# 使用启动脚本启动Rasa和Nginx
CMD ["sh","start.sh"]



