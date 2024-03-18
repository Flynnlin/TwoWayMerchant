# 使用官方 Python 3.8 镜像作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装项目依赖项
RUN pip install Django==4.2.11 \
                asgiref==3.7.2 \
                backports.zoneinfo==0.2.1 \
                et-xmlfile==1.1.0 \
                openpyxl==3.1.2 \
                Pillow==10.2.0  \
                mysqlclient==2.2.4 \
                sqlparse==0.4.4 \
                typing-extensions==4.10.0 \
                tzdata==2024.1 \
                wheel==0.43.0 \
                django-mdeditor==0.1.20  \
                markdown==3.6 \

# 暴露容器的 8000 端口
EXPOSE 8000

# 执行数据库迁移命令
RUN python manage.py makemigrations && \
    python manage.py migrate

# 设置容器启动时的命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
