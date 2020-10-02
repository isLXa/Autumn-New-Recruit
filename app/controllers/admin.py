'''
定义admin对象
'''
from flask import Blueprint, request, jsonify, make_response
from app.services import database
from flask import session
import pandas as pd
import io
import xlsxwriter

admin_bp = Blueprint('admin',__name__,url_prefix='/admin')

@admin_bp.route('/session', methods = ['post'])
def login_admin():
    data : dict = request.get_json(force = True)
    username : str = data['username']
    password : str = data['password']
    try:
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
            })
    except:
        return jsonify({
            "statue": 500,
            "msg": "服务器错误",
            "data": None
        })

@admin_bp.route('/user/count', methods = ['get'])
def query_admin():
    if not session.get('login'):
        return jsonify({
            "statue":401,
            "msg":"未登录",
            "data":None
        })
    try:
        data:dict = database.query_admin()
        return jsonify({
            "status": 200,
            "msg": "查询成功",
            "data": data
        })
    except:
        return jsonify({
            "statue": 500,
            "msg": "服务器错误",
            "data": None
        })

@admin_bp.route('/user/excel', methods = ['get'])
def get_excel():
    if not session.get('login'):
        return jsonify({
            "statue":401,
            "msg":"未登录",
            "data":None
        })
    data = database.get_excel()
    df = pd.DataFrame(data = data, columns=['姓名','电话','性别','年级','学院','寝室','第一志愿','第二志愿','是否服从调剂','自我介绍'])
    bio = io.BytesIO()
    writer = pd.ExcelWriter(bio, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='结果汇总')
    writer.save()

    bio.seek(0)  # 文件指针
    rv = make_response(bio.getvalue())
    bio.close()

    # mime_type = mimetypes.guess_type(results)[0]  # 文件类型
    rv.headers['Content-Type'] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    rv.headers["Cache-Control"] = "no-cache"
    rv.headers['Content-Disposition'] = 'attachment; filename={}.xlsx'.format('Output')

    return rv