'''
相应数据库操作
users：增、删、改、查；
admin：查（登录，数据查询）
'''
from app.extensions import db
from app.models import Admin,User
from flask import session
from io import BytesIO
import xlwt

def check_tel(tel : str):
    user = User.query.filter(User.tel == tel).count()
    if user == 1:
        return False
    else:
        return True

def add_user(name, tel, sex, grade, college, dormitory, first, second, adjust, description):
    user = User(name=name, tel=tel, sex=sex, grade=grade, college=college, dormitory=dormitory, first=first,
                second=second,adjust=adjust,description=description)
    db.session.add(user)
    db.session.commit()

def updata_user(name,tel, sex, grade, college, dormitry, first, second, adjust, description):
    user = User.query.filter(User.username==name and User.tel==tel).first()
    user.sex = sex
    user.grade = grade
    user.college=college
    user.dormitory=dormitry
    user.first=first
    user.second=second
    user.adjust=adjust
    user.description=description
    db.session.add(user)
    db.session.commit()

def query_user(name,tel):
    user = User.query.filter(User.username == name, User.tel == tel).first()
    ret = []
    if not user:
        ret = {"username":user.username, "tel":user.tel, "sex":user.sex, "grade":user.grade, "college":user.college,
               "dormitory":user.dormitory, "first":user.first, "second":user.second, "adjust":user.adjust,
               "description":user.description}
    return ret

def login_admin(name, password):
    admin = Admin.query.filter(Admin.username==name, Admin.password == password).count()
    if admin == 0:
        session['login']= False
    else:
        session['login'] = True
        session['name'] = name


def query_admin():
    data = ['技术部']
    ret = []
    for i in data:
        fcount = User.query.filter(User.first == i).count()
        scount = User.query.filter(User.second == i).count()
        ret.append({"dapartment": i, "first":fcount, "second":scount})
    return ret

def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def get_excel():
    if session.get('name') == '管理员':
        result = User.query.all()
        sheet_name = '全部门'
    else:
        result = User.query.filter(User.first == session['name']).all()
        sheet_name = session['name']
    style = set_style('微软雅黑', 220, True)
    f = xlwt.Workbook()
    sheet = f.add_sheet(sheetname=sheet_name+'报名统计表', cell_overwrite_ok=True)
    header = ['姓名','电话','性别','年级','学院','寝室','第一志愿','第二志愿','是否服从调剂','自我介绍']
    #写头
    for i in range(0, len(header)):
        sheet.write(0, i, header[i], style)#行，列，列名,样式

    idx = 1
    data = []
    for user in result:
        ret = [ user.name, user.tel, user.sex, user.grade, user.college, user.dormitory, user.first, user.second,
                user.adjust, user.description]
        data.append(ret)
        for i in range(0,len(ret)):
            sheet.write(idx,i,ret[i])
        idx += 1
    f.save('./excels/'+sheet_name+'报名统计表'+'.xls')
    return data