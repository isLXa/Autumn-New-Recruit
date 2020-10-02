"""
相应数据库操作
users：增、删、改、查；
admin：查（登录，数据查询）
"""
from app.extensions import db
from app.models import Admin, User
from flask import session
import xlwt
import io


def check_tel(tel: str):
    user = User.query.filter(User.tel == tel).count()
    if user == 1:
        return False
    else:
        return True


def add_user(data: dict):
    user = User(**data)
    db.session.add(user)
    db.session.commit()


def updata_user(name, tel, sex, grade, college, dormitry, first, second, adjust, description):
    user = User.query.filter(User.name == name and User.tel == tel).first()
    user.sex = sex
    user.grade = grade
    user.college = college
    user.dormitory = dormitry
    user.first = first
    user.second = second
    user.adjust = adjust
    user.description = description
    db.session.commit()


def query_user(name, tel):
    user = User.query.filter(User.name == name, User.tel == tel).first()
    if not user:
        return {}
    return {"name": user.name, "tel": user.tel, "sex": user.sex, "grade": user.grade,
            "college": user.college,
            "dormitory": user.dormitory, "first": user.first, "second": user.second, "adjust": user.adjust,
            "description": user.description}


def login_admin(name, password):
    admin = Admin.query.filter(Admin.username == name, Admin.password == password).count()
    if admin == 0:
        session['login'] = False
    else:
        session['login'] = True
        session['name'] = name


def query_admin():
    if session.get('name') == 'admin':
        depart_names = db.session.query(User.first).group_by(User.first).all()
    else:
        depart_names = [(session.get('name'),)]

    return [{
        'dapartment': depart_name[0],
        'first': User.query.filter(User.first == depart_name[0]).count(),
        'second': User.query.filter(User.first != depart_name[0], User.second == depart_name[0]).count()
    } for depart_name in depart_names]


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def get_excel():
    if session.get('name') == 'admin':
        result = User.query.all()
        sheet_name = '全部门'
    else:
        result = User.query.filter(User.first == session['name']).all()
        sheet_name = session['name']

    style = set_style('微软雅黑', 220, True)
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet(sheetname=sheet_name + '报名统计表', cell_overwrite_ok=True)
    header = ['姓名', '电话', '性别', '年级', '学院', '寝室', '第一志愿', '第二志愿', '是否服从调剂', '自我介绍']
    # 写头
    for i in range(0, len(header)):
        sheet.write(0, i, header[i], style)  # 行，列，列名,样式
    idx = 1
    data = []
    for user in result:
        ret = [user.name, user.tel, user.sex, user.grade, user.college, user.dormitory, user.first, user.second,
               '是' if user.adjust else '否', user.description]
        data.append(ret)
        for i in range(0, len(ret)):
            sheet.write(idx, i, ret[i])
        idx += 1
    buf = io.BytesIO()
    f.save(buf)
    return buf
