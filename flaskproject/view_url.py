from flask import Flask
from flask import render_template
import datetime
app=Flask(__name__)

@app.route("/index/") #路由
def index():
    return render_template('index.html',**locals())
@app.route("/userInfo/") #路由
def userInfo():
    return render_template('userInfo.html',**locals())

@app.route('/list/')
def list():
    return 'hello list'

@app.route('/content/<username>/<int:age>')
def content(username,age):
    return "hello,he is %s,he is %s years old"%(username,age)

@app.route('/birthday/<birthday>/')
def birthday(birthday):
    dd=birthday
    dd=datetime.datetime.strptime(dd,'LLL')
    return '他的生日是 %s'%(birthday)

@app.route('/base/')
def base():
    return render_template('base.html',**locals())

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)