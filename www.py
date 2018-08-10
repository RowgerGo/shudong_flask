from application import app
from api.v1.controller.index import route_index
from api.v1.controller.user.User import route_user

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')

