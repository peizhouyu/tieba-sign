# tieba-sign

#### 项目介绍
百度贴吧 自动签到脚本

#### 软件架构
软件架构说明

##### 添加docker部署方式
- 镜像地址: https://hub.docker.com/r/peizhouyu/tieba-sign
- 启动方式: `docker run -itd -e BDUSS=[your_bduss] -e MYID=[your_id] -e EXEC_TIME=[Timed task execution time] peizhouyu/tieba-sign:1.1 bash`
- 例示: `docker run -itd -e BDUSS=abcder -e MYID=大雪无痕 -e EXEC_TIME=20:00 peizhouyu/tieba-sign:1.1 bash`


