"""
定义users对象
"""
from flask import Blueprint, request, jsonify
from app.services import check, database

# 构建蓝图
users_bp = Blueprint('users', __name__, url_prefix='/user')


# 报名
@users_bp.route('', methods=['post'])
def add_user():
    data: dict = request.get_json(force=True)
    tel: str = data['tel']
    if not check.check_tel(tel):
        return jsonify({
            "status": 400,
            "msg": "手机号错误",
            "data": None
        }), 400

    if not database.check_tel(tel):
        return jsonify({
            "status": 409,
            "msg": "该手机号已报名",
            "data": None
        }), 409

    database.add_user(data)
    return jsonify({
        "status": 200,
        "msg": "报名成功",
        "data": None
    })


@users_bp.route('', methods=['get'])
def query_user():
    tel = request.args.get('tel')
    name = request.args.get('name')
    if not check.check_tel(tel):
        return jsonify({
            "status": 404,
            "msg": "手机号错误",
            "data": None
        }), 404

    data: dict = database.query_user(name, tel)
    if not data:
        return jsonify({
            'status': 404,
            'msg': '报名信息不存在',
            'data': None
        }), 404

    return jsonify({
        "status": 200,
        "msg": "查询成功",
        "data": data
    })


@users_bp.route('', methods=['put'])
def updata():
    data: dict = request.get_json(force=True)
    name: str = data['name']
    tel: str = data['tel']
    sex: str = data['sex']
    grade: str = data['grade']
    campus: str = data['campus']
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
        }), 404
    print('update')
    database.update_user(name, tel, sex, grade,campus, college, dormitory, first, second, adjust, description)
    return jsonify({
        "status": 200,
        "msg": "修改成功",
        "data": None
    })
