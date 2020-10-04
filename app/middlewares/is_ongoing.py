import datetime
from app.config import BaseConfig
from app.extends.error import HttpError


def is_ongoing():
    begin = datetime.datetime.strptime(BaseConfig.begin, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(BaseConfig.end, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    if now < begin:
        raise HttpError(410, '活动还未开始')
    elif now > end:
        raise HttpError(410, '活动已结束')
