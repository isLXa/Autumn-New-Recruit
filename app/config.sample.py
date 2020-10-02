"""
数据库信息
"""
dbconfig = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,
    'database': ''
}


class AppConfig:
    # 动态追踪数据库的修改，解决控制台的提示
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4' \
        .format(**dbconfig)
    SECRET_KEY = ''
