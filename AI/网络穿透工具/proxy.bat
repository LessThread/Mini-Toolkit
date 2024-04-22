@echo off

REM 设置远程服务端的IP地址、用户名和SSH端口号
set REMOTE_HOST=127.0.0.1
set REMOTE_USER=root
set REMOTE_PORT=22

REM 设置本地和远程端口号
set LOCAL_PORT1=11111
set REMOTE_PORT1=11111

set LOCAL_PORT2=7860
set REMOTE_PORT2=7860

rem 获取当前用户的 HOME 目录
for %%I in (%USERPROFILE%) do set HOME=%%~fI

rem 确保 .ssh 文件夹存在
if not exist "%HOME%\.ssh\" mkdir "%HOME%\.ssh"

echo 正在拷贝 key 文件拷贝到 %HOME%\.ssh\ 目录下

rem 拷贝 key 文件
copy /y ".\KeyPair-use_for_web_server.pem" "%HOME%\.ssh\"


REM 设置密钥文件路径
set PRIVATE_KEY_FILE=%HOME%\.ssh\KeyPair-use_for_web_server.pem


echo 正在建立连接
echo ssh -o StrictHostKeyChecking=no -i %PRIVATE_KEY_FILE% -L %LOCAL_PORT1%:127.0.0.1:%REMOTE_PORT1% -L %LOCAL_PORT2%:127.0.0.1:%REMOTE_PORT2% %REMOTE_USER%@%REMOTE_HOST% -p %REMOTE_PORT% -vvv

REM 使用建立SSH隧道 /home/ma-user/work/mindformers/chat_web
ssh -o StrictHostKeyChecking=no  -i %PRIVATE_KEY_FILE% -L %LOCAL_PORT1%:127.0.0.1:%REMOTE_PORT1% -L %LOCAL_PORT2%:127.0.0.1:%REMOTE_PORT2% %REMOTE_USER%@%REMOTE_HOST% -p %REMOTE_PORT% -N -vvv
