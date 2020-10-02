"""
检查传入信息
"""


def check_tel(tel: str):
    tel = str(tel)
    return tel.isdigit() and tel[0] == '1' and len(tel) == 11
