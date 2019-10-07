import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIR = os.path.join(BASE_DIR,"static")
class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")#数据库地址sqllite
    SQLALCHEMY_TRACK_MODIFICATIONS =True #falsk1版本之后，添加的选项，目的是跟着修改

class RunConfig(Config):
    DEBUG = False