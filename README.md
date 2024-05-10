# flaskOCR

## 本地部署

环境要求：python 3.10 以上，安装了 poetry

若未安装poetry，请

```shell
pip install poetry
```

初始化环境

```shell
poetry install
```

初始化数据库

```shell
flask init
```

启动

```shell
flask run
```


## TODO
#### ~~1.所有模块接口及前端的路由~~
#### ~~2.完善数据库(连接mysql, 修改表结构，使其成功初始化数据)~~
#### ~~3.在2.完成的前提下，修改登录、权限等模块~~
#### 4.美化首页(工作空间等)，删除不必要组件

## 开发日志
#### 2024/5/9 11:10 数据库修改，添加注册功能，完善前端及其部分接口
#### 2024/5/10 16:00 所有功能接口已完善（车辆检测还在尝试本地yolo）

## 工作分配
### S: 
1. orms下所有数据表字段的定义（了解主外键约束）  
### L: 
1. apis下passport登录注册路由  
2. extensions下init_jwt（了解token及jwt工作机制）
### CH: 
1. apis下right、role、user路由的更删改查
2. extensions下init_db和init_script（数据库init建表）