from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os

class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Application,self).__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        #将数据信息配置在db_cofnig中，此文件不上传到git,需要新建db_config.py文件，并且拷贝下面内容，
        #SERVER_PORT=8999
        #SQLALCHEMY_DATABASE_URI='mysql://root:123445@127.0.0.1/mysql'
        #SQLALCHEMY_TRACK_MODIFICATIONS=False
        self.config.from_pyfile('config/db_config.py')
        db.init_app(self)

db=SQLAlchemy()

app=Application(__name__,template_folder=os.getcwd()+"/app/templates/",root_path=os.getcwd())

manager=Manager(app)


# 函数模板
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl,'buildUrl')