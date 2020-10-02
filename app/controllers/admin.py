"""
定义admin对象
"""
from flask import Blueprint, request, jsonify, make_response
from app.services import database
from flask import session

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/session', methods=['post'])
def login_admin():
    data: dict = request.get_json(force=True)
    username: str = data['username']
    password: str = data['password']
    database.login_admin(username, password)
    if session.get('login'):
        return jsonify({
            "statue": 200,
            "msg": "登录成功",
            "data": None
        })
    else:
        return jsonify({
            "statue": 404,
            "msg": "用户名或者密码错误",
            "data": None
        }), 404


@admin_bp.route('/user/count', methods=['get'])
def query_admin():
    if not session.get('login'):
        return jsonify({
            "statue": 401,
            "msg": "未登录",
            "data": None
        }), 401

    data: dict = database.query_admin()
    return jsonify({
        "status": 200,
        "msg": "查询成功",
        "data": data
    })


@admin_bp.route('/user/excel', methods=['get'])
def get_excel():
    if not session.get('login'):
        return jsonify({
            "statue": 401,
            "msg": "未登录",
            "data": None
        }), 401
    buf = database.get_excel()
    resp = make_response(buf.getvalue())
    buf.close()
    resp.headers['Content-Type'] = "application/vnd.ms-excel"
    resp.headers["Cache-Control"] = "no-cache"
    resp.headers['Content-Disposition'] = 'attachment; filename={}.xls'.format('Output')
    return resp
