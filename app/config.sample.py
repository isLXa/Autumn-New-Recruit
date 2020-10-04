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


class BaseConfig:
    begin = "2020-5-23 0:00:00"
    end = "2020-5-23 0:00:00"


class AppConfig:
    # 动态追踪数据库的修改，解决控制台的提示
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4&collation=utf8mb4_general_ci'.format(
        **dbconfig)
    SECRET_KEY = ''
