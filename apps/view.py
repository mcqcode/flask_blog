from flask import Blueprint, render_template, url_for, request
import hashlib

from apps.modle import User
from ext import db

user_bp = Blueprint('user',__name__)

@user_bp.route('/')
def user_center():
    return render_template('usercenter/user_page.html')

@user_bp.route('/register',methods=['POST','GET'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        sex = request.form.get('sex')
        if password ==repassword:
            result = User.query.filter_by(username = username).first()
            if result == None:
                user = User()
                user.username = username
                user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                user.phone = phone
                user.sex = sex
                user.level = False
                db.session.add(user)
                db.session.commit()
                return render_template('usercenter/register.html',msg = '注册成功！')
            else:
                return render_template('usercenter/register.html',msg ='用户已存在!')

        return render_template('usercenter/register.html', msg='密码不一致，请重新注册!')
    else:
        return render_template('usercenter/register.html')
@user_bp.route('/login',methods=['POST','GET'])
def user_login():
    return render_template('usercenter/login.html')