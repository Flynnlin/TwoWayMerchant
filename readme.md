# What is it？


# startup
1. 创建本地配置文件`local_setting.py`,位于TwoWayMerchant下
    ```
    #mysql数据库，MySQL 8 or later is required
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.mysql",   #数据库类型
    #         "NAME": "TwoWayMerchant",                        #数据库名
    #         "USER": "ORM",              #用户名
    #         "PASSWORD": "12",       #密码
    #         "HOST": "127.0.0.1",        #ip
    #         "PORT": "3306",             #端口
    #     }
    # }
    ALLOWED_HOSTS = ['server_ip']
    USERNAME = ["1","2"]
    PASSWORD = "123"
    ```


2. docker 运行
    ```
    #数据库（可选
    docker run -d --name mysql_8 -e MYSQL_ROOT_PASSWORD=123 -p 3306:3316 --restart always mysql:8
    ```
    创建docker容器
    ```
    docker build -t twowaymerchant .
    docker run -d -p 8000:8000 --restart always --name=merchant twowaymerchant
    ```
3. 更新
   ```cmd
   docker stop merchant
   docker rm merchant
   git pull
   docker build -t twowaymerchant .
   docker run -d -p 8000:8000 --restart always --name=merchant twowaymerchant
   ```