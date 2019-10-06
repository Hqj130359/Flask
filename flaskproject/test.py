# import datetime
# result=[]  #接受所有的日期，需要一个嵌套列表，列表当中嵌套的是7元素列表
# #月份分类
# big_month=[1,3,5,7,8,10,12]
# small_month=[4,6,9,11]
#
# now=datetime.datetime.now()
# month=now.month
# first_date=datetime.datetime (now.year,now.month,1,0,0)
#     #年月日 时 分
# # print(first_date.weekday()) #python的日期当中 星期的范围 0-6  0是周一  6 代表周日
# # print(now.weekday())
# # first_week=first_date.weekday() #2019年9月1号是周日
#     #如果一号是周一  那么第一行应该是 1-7号    0
#     #如果一号是周二  那么第一行应该是 1*empty+1-6号 1
#     #如果一号是周三  那么第一行应该是 2*empty+1-5号 2
#     #如果一号是周四  那么第一行应该是 3*empty+1-4号 3
#     #如果一号是周五  那么第一行应该是 4*empty+1-3号 4
#     #如果一号是周六  那么第一行应该是 5*empty+1-2号 5
#     #如果一号是周日  那么第一行应该是 6*empty+1号  6
#
# if month  in big_month:
#     day_range=range(1,32) #指定月份的总天数
# elif month in small_month:
#     day_range=range(1,31)
# else:
#     day_range=range(1,29)
# # 获取指定月天数
# day_range=list(day_range)
#
# first_week=first_date.weekday() #获取指定月1号是周几 6
# line1=[] #第一行数据
# #day_range  1-30
# for e in range(first_week):
#     line1.append('empty')
# for d in range(7-first_week):
#     line1.append(str(day_range.pop(0)))
# # print(line1)
# result.append(line1)
#
# while day_range :# 如果总天数列表有值，就接着循环
#     line=[] #每个子列表
#     for i in range(7):
#         if len(line) < 7 and day_range:
#             line.append(str(day_range.pop(0)))
#         else:
#             line.append('empty')
#     result.append(line)
# # print(result)
# # 展示效果
# print("星期一 星期二 星期三 星期四 星期五 星期六 星期日")
# for line in result:
#     for day in line:
#         day=day.center(6)
#         print(day,end="  ")
#     print()

# import calendar
# result=calendar.month(19,9).splitlines()[2:]
# for line in result:
#     print(line)
from flask import Flask,render_template
import datetime
# import calendar
app=Flask(__name__)

class Calendar:
    """
    当前类实现日历功能
    1返回列表嵌套列表的日历
    2,安装日历格式打印日历
    """

    def __init__(self, month='now'):
        self.result = []  # 接受所有的日期，需要一个嵌套列表，列表当中嵌套的是7元素列表
        # 月份分类
        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]

        # 获取当前月
        now = datetime.datetime.now()
        if month == "now":
            month = now.month
            first_date = datetime.datetime(now.year, now.month, 1, 0, 0)
        # 年月日 时 分
        # print(first_date.weekday()) #python的日期当中 星期的范围 0-6  0是周一  6 代表周日
        # print(now.weekday())
        # first_week=first_date.weekday() #2019年9月1号是周日
        # 如果一号是周一  那么第一行应该是 1-7号    0
        # 如果一号是周二  那么第一行应该是 1*empty+1-6号 1
        # 如果一号是周三  那么第一行应该是 2*empty+1-5号 2
        # 如果一号是周四  那么第一行应该是 3*empty+1-4号 3
        # 如果一号是周五  那么第一行应该是 4*empty+1-3号 4
        # 如果一号是周六  那么第一行应该是 5*empty+1-2号 5
        # 如果一号是周日  那么第一行应该是 6*empty+1号  6
        else:
            # assert int(month) in range(1,13)
            first_date = datetime.datetime(now.year, month, 1, 0, 0)

        if month in big_month:
            day_range = range(1, 32)  # 指定月份的总天数
        elif month in small_month:
            day_range = range(1, 31)
        else:
            day_range = range(1, 29)

        # 获取指定月天数
        self.day_range = list(day_range)
        first_week = first_date.weekday()  # 获取指定月1号是周几 6

        line1 = []  # 第一行数据
        for e in range(first_week):
            line1.append('empty')
        for d in range(7 - first_week):
            line1.append(str(self.day_range.pop(0)))
        self.result.append(line1)
        while self.day_range:  # 如果总天数列表有值，就接着循环
            line = []  # 每个子列表
            for i in range(7):
                if len(line) < 7 and self.day_range:
                    line.append(str(self.day_range.pop(0)))
                else:
                    line.append('empty')
            self.result.append(line)

    def return_month(self):
        """

        :return:
        """
        return self.result

    def print_month(self):
        """
        :return:
        """
        print("星期一 星期二 星期三 星期四 星期五 星期六 星期日")
        for line in self.result:
            for day in line:
                day = day.center(6)
                print(day, end="  ")
            print()

@app.route("/userInfo/")
def userInfo():
    calendar=Calendar().return_month()
    return render_template("userInfo.html",**locals())


print(1)
if __name__ == "__main__":
  app.run(host='127.0.0.1',port=8000,debug=True)