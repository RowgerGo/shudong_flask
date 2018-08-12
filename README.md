# flask-shudong

#### 项目介绍
flask-shudong树洞app和微信公众号接口api

#### 软件架构
软件架构说明


#### 安装教程

1. pip install pipenv
2. pipenv install
3. 使用pycharm打开项目，设置环境（pipenv --venv 查看路径）

#### 需要安装的包
```
flask = "*"
flask-sqlalchemy = "*"
flask-script = "*"
```
使用`conda install mysqlclient`来安装mysqlclient，因为在Windows下使用pip安装mysqlclient报错
```
pip install pymysql
```
```
python manager.py runserver
```
使用flask-sqlacodegen自动生成model
```
flask-sqlacodegen  mysql+pymysql://root:123456@118.24.126.15:3306/hahh --tables yi_admin --outfile "common/models/user.py" --flask
```
#### 参与贡献

