# Divine-Rhythm-Chatbot
A chatbot based on the RASA framework called Divine Rhythm.Divine Rhythm chatbot  aims to automate the process of delivering information about different subscription plans and handling related customer complaints. The "chatbot" is envisioned to be an integrated feature in the company's primary app, focusing primarily on first-time users but catering to existing ones as well. The bot will also offer multiple channels for customer support, from live human intervention to email and phone support, in case it cannot resolve an issue.You can use your computer's browser to access http://118.25.46.156:8088/ to enter our bot interface.
## The environment of my computer before installing RASA
Python 3.8.10 pip 23.2.1
## Create virtual environment
### 1. Make a instance named venv
python -m venv venv
### 2.Enter the directory of the virtual environment
cd venv\Scripts
## 3.Activate virtual environment
activate.bat
## Install Rasa
pip3 install rasa
## Initialize RASA
rasa init
## Train the model
rasa train
## Start server
### 1.Run action server
rasa run actions
### 2.Run rasa server
rasa run --enable-api --cors "*"
## Install and Configure Nginx
### 1.Activate nginx
start nginx
### 2.Modify the configuration file.
server {
    listen 80;
    charset utf-8;
location / {
    root /app/;
    index  index.html index.htm;
}
location /webhook {
     proxy_pass http://rasa:5005;
     proxy_set_header Host $host;
}
location /socket.io {
    proxy_pass http://rasa:5005/socket.io;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
}
### 3.Reload nginx
nginx.exe -s reload
# Here you can open your browser to http://118.25.46.156:8088/, you can in the cloud for all to use to our bot.
