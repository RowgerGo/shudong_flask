from flask import Blueprint,render_template,request,jsonify
from application import app
from celery import Celery
from flask_mail import Message,Mail
from common.libs.Utils.RespUtils import RespUtils

route_auth_user = Blueprint( 'route_auth_user_api',__name__ )

@route_auth_user.route( "/index" ,methods=["POST"])
def index():
    if request.method == 'GET':
        return RespUtils.error('不支持get请求')

    # send the email
    req = request.values
    email = req['email'] if 'email' in req else ""
    if email is None or len(email) < 1:
        return RespUtils.error("请输入正确的邮箱地址~~")
    msg = Message('Hello from Flask',
                  recipients=[email])
    msg.body = 'This is a test email sent from a background Celery task.'

    send_async_email.delay(msg)


@Celery.task
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    with app.app_context():
        Mail.send(msg)