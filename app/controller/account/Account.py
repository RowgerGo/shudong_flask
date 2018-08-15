# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request
from common.libs.Utils.RespUtils import RespUtils
from common.libs.user.UserService import UserService
from common.libs.Helper import getCurrentData
from common.models.user import YiAdmin

from application import app,db

route_account = Blueprint( 'account_page',__name__ )

@route_account.route( "/index" )
def index():
    return render_template( "account/index.html" )

@route_account.route( "/info" )
def info():
    return render_template( "account/info.html" )

@route_account.route( "/set" )
def set():
    return render_template( "account/set.html" )

@route_account.route( "/add",methods=["POST"] )
def add():
    req=request.values
    username=req['username'] if 'username' in req else ""
    password = req['password'] if 'password' in req else ""
    email = req['email'] if 'email' in req else ""
    salt=UserService.geneSalt()

    module_user=YiAdmin()
    module_user.username=username
    module_user.password=UserService.genePwd(password,salt)
    module_user.email=email
    module_user.level='1'
    module_user.state='2'
    module_user.admin='3'
    module_user.login_salt=salt
    module_user.lasttime=getCurrentData()
    try:
        db.session.add(module_user)
        db.session.commit()
    except Exception as e:
        return RespUtils.error('添加失败', e)

    return  RespUtils.success('添加成功')

