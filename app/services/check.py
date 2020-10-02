'''
检查传入信息
'''
from app.services import database
def check_tel(tel : str):
    if tel[0] is not '1':
        return False
    else:
        return True

def check_name(name: str):
    if 1 < name.count() < 7:
        return False
    else:
        return True


