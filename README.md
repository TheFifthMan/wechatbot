# 基于Flask建设微信公众号

# 配置
```
在项目下面新建 .env 文件
WECHAT_TOKEN=xxxx
AES_KEY=xxx
APPID=xxxxx
TULING_APIKEY=7xxxxx
```
# supervisor 配置

```
[program:wechatbot]
command=/home/ubuntu/microblog/venv/bin/gunicorn -b localhost:8000 -w 4 microblog:app
directory=/home/ubuntu/microblog
user=ubuntu
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stdout_logfile = /var/log/supervisor/wechatbot.log
stderr_logfile = /var/log/supervisor/wechatbot_err.log
redirect_stderr = true
startsecs = 3
environment = LC_ALL="en_US.UTF-8"
```

