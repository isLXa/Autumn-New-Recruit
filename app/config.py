'''
数据库信息
'''
dbconfig = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'port': 3306,
    'database': 'bbt'
}


class AppConfig:
    #动态追踪数据库的修改，解决控制台的提示
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4' \
        .format(**dbconfig)


class AppTestConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True
