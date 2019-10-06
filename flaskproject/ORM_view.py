import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)  #实例化app

#配置参数
BASE_DIR=os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASE_DIR,"ORM.sqlite")
# 数据库地址sqlite
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:111111@localhost/demo3" #数据库地址

app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True #请求结束后自动提交
app.config["SQLALCHEMY_PTACK_MODIFICATIONS"]=True #flask1版本之后 添加的选项，目的是跟踪修改

#orm关联应用
models=SQLAlchemy(app)

#定义表
class Curriculun(models.Model):
    __tablename__="curriculum"
    id=models.Column(models.Integer,primary_key=True)
    c_id=models.Column(models.String(32))
    c_name=models.Column(models.String(32))
    c_time=models.Column(models.Date)


import datetime
session=models.session()#创建操作数据库的会话

c1=Curriculun(c_id = "0002",c_name="html",c_time=datetime.datetime.now())
c2=Curriculun(c_id = "0003",c_name="mysql",c_time=datetime.datetime.now())
c3=Curriculun(c_id = "0004",c_name='linux',c_time=datetime.datetime.now())

session.add_all([c1,c2,c3])
session.commit()
# # 查所有
# all_c = Curriculun.query.all()
# for c in all_c:
#     print(c.id,c.c_name)
# # 条件查询
# all_c=Curriculun.query.query.filter_by(c_id='0002')#返回列表对象
# for c in all_c:
#     print(c.id,c.c_name)
#
# # 查询一条
# c=Curriculun.query.get(10) #返回列表对象
# print(c)
# print(c.id,c.c_name)
#
# c=Curriculun.query.firsy()
# print(c.id,c.c_name)
#
# #排序
# all_c=Curriculun.query.order_by('id')
# # all_c = Curriculun.query.order_by(models.desc('id'))#倒序
#
# for c in all_c:
#     print(c.id,c.c_name)
#
# all_c=Curriculun.query.offset(2).limit(2).all() #倒序
    # offset 便宜，在这里指的时候查询的起始位置
    # limit 具体查询的数量
# select * from  curriculum limit 0,2  #从0号索引开始，查询两条
# for c in all_c:
#     print(c.id,c.c_name)
#
# #删除数据
# c=Curriculun.query.get(4)
# print(c)
# session.delete(c)
# session.commit()
# #修改数据
# c=Curriculun.query.get(3)
# c.c_name='MySQL'
# session.add(c)
session.commit()

#创建表（同步）
# models.create_all()