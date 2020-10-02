'''
定义users对象
'''
from flask import Blueprint, request, jsonify
from app.services import check,database

#构建蓝图
users_bp = Blueprint('users', __name__, url_prefix='/user')

#报名
@users_bp.route('', methods = ['post'])
def add_user():
    data: dict = request.get_json(force = True)
    name : str = data['name']
    tel: str = data['tel']
    sex : str = data['sex']
    grade : str = data['grade']
    college : str = data['college']
    dormitory : str = data['dormitory']
    first : str = data['first']
    second : str = data['second']
    adjust : int = data['adjust']
    description : str = data['description']
    if not check.check_tel(tel):
        return jsonify({
            "status": 400,
            "msg": "手机号错误",
            "data": None
        })
    if not database.check_tel(tel):
        return jsonify({
            "status": 409,
            "msg": "该手机号已报名",
            "data": None
        })
    try:
        database.add_user(name, tel, sex, grade, college, dormitory, first, second, adjust, description)
        return jsonify({
            "status": 200,
            "msg": "报名成功",
            "data": None
        })
    except:
        return jsonify({
            "statue":500,
            "msg":"服务器错误",
            "data":None
        })

@users_bp.route('/<tel>/<name>', methods =['get'])
def query_user(tel : str, name: str):
    if not check.check_tel(tel):
        return jsonify({
            "status": 404,
            "msg": "手机号错误",
            "data": None
        })
    try:
        data:dict = database.query_user(name,tel)
        return jsonify({
            "status": 200,
            "msg": "查询成功",
            "data": data
        })
    except:
        return jsonify({
            "statue":500,
            "msg":"服务器错误",
            "data":None
        })

@users_bp.route('', methods = ['put'])
def updata():
    data : dict = request.gey_json(force = True)
    name: str = data['name']
    tel: str = data['tel']
    sex: str = data['sex']
    grade: str = data['grade']
    college: str = data['college']
    dormitory: str = data['dormitory']
    first: str = data['first']
    second: str = data['second']
    adjust: int = data['adjust']
    description: str = data['description']
    if not check.check_tel(tel):
        return jsonify({
            "status": 404,
            "msg": "手机号错误",
            "data": None
        })
    try:
        database.updata_user(name, tel, sex, grade, college, dormitory, first, second, adjust, description)
        return jsonify({
            "status": 200,
            "msg": "修改成功",
            "data": None
        })
    except:
        return jsonify({
            "statue": 500,
            "msg": "服务器错误",
            "data": None
        })