@echo off
REM 切换到 Redis 安装目录
cd /d %REDIS_DIR%

REM 启动 Redis 服务器
redis-server.exe redis.windows.conf

REM 暂停以查看输出
pause
