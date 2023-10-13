#!/bin/sh

# 启动Rasa服务
rasa run --enable-api --cors '*' &

# 启动Nginx
python -m http.server
