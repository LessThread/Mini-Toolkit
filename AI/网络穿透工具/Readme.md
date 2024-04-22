**请注意,由于超算容器设置,ssh可能导致指纹不一致问题,如果无法建立隧道,请删除本机的known_host**



1. 启动后端
    - 请按照流程启动run_chat_server.py  
    - 执行下面命令也可以启动,不保证稳定性  
    - `sh /home/ma-user/work/mindformers/chat_web/script/start.sh`

2. 建立隧道
    - 在本机powershell/cmd中执行 `./proxy.bat`
    
3. 启动前端
    - 等待后端启动完成后,在本机运行`python .\run_chat_web_demo.py`(提示,请确保python环境完整)
    - 浏览器访问`http://localhost:8080/`