from application import app

'''
统一拦截器
'''
from app.interceptors.AuthInterceptor import *


'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from app.controller.index import route_index
from app.controller.user.User import route_user
from app.controller.static import route_static
from app.controller.account.Account import route_account

from app.controller.finance.Finance import route_finance
from app.controller.food.Food import route_food
from app.controller.member.Member import route_member
from app.controller.stat.Stat import route_stat

'''
app的api接口
'''
from app.controller.api.auth.user import route_auth_user



app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_account,url_prefix='/account')

app.register_blueprint(route_finance,url_prefix='/finance')
app.register_blueprint(route_food,url_prefix='/food')
app.register_blueprint(route_member,url_prefix='/member')
app.register_blueprint(route_stat,url_prefix='/stat')

app.register_blueprint(route_auth_user,url_prefix='/api/auth/user')