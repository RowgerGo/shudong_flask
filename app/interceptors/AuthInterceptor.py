from application import app
from flask import request

@app.before_request
def before_request():
    path = request.path
    check_login()



def check_login():
    cookies=request.cookies
    auth_cookie= cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else ""
    app.logger.info('----------------------')
    app.logger.info(cookies)
