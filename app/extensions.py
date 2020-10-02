from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import Session, Query

cors = CORS(supports_credentials=True)


# 下面和db=SQLAlchemy()等价，只是给一些对象添加了类型注解，写代码的时候编辑器能自动补全
class _SQLAlchemy(SQLAlchemy):
    session: Session


db = _SQLAlchemy()


class Model(db.Model):
    __abstract__ = True

    query: Query

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
