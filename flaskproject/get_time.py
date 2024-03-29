# import datetime
# #接受所有的日期，需要一个嵌套列表，列表当中嵌套的是7元素列表
# result=[]
# #月份分类
# big_month=[1,3,5,7,8,10,12]
# small_month=[4,6,9,11]
#
# now=datetime.datetime.now()
# month=now.month
# first_date = datetime.datetime(now.year,now.month,1,0,0)
#     # 年 月 日 时 分
# # month=int(input('输入月份:'))
# if month in big_month:
#     day_range = range(1,32)
# elif month in small_month:
#     day_range = range(1,31)
# else:
#     day_range = range(1, 29)
# #获取指定月天数
# day_range=list(day_range)
#
# # print(first_date.weekday()) #python的日期当中 星期范围 0-6 0代表周一
# first_week = first_date.weekday() #2019年9月1号是周日
# line1=[] #第一行数据
#     #如果一号周周一那么第一行1-7号   0
#     # 如果一号周周二那么第一行empty*1+1-6号  1
#     # 如果一号周周三那么第一行empty*2+1-5号  2
#     # 如果一号周周四那么第一行empty*3+1-4号  3
#     # 如果一号周周五那么第一行empyt*4+1-3号  4
#     # 如果一号周周六那么第一行empty*5+1-2号  5
#     #如果一号周日那么第一行empty*6+1号   6
#     #输入 1月
#         #得到1月1号是周几
#         #[] 填充7个元素 索引0对应周一
#         #返回列表
# #day_range 1-30
# for e in range(first_week):
#     line1.append('empty')
# for d in range(7-first_week):
#     line1.append(str(day_range.pop(0)))
# print(line1)
# result.append(line1)
#
# #添加第二行到最后一行
# while day_range: #如果总天数列表有值，就接着循环
#     line=[] #每个字列表
#     for i in range(7):
#         if len(line) < 7 and day_range:
#             line.append(str(day_range.pop(0)))
#         else:
#             line.append('empty')
#     result.append(line)
#
# #s只是为了展示效果
# print('星期一  星期二  星期三  星期四  星期五  星期六  星期日')
# for line in result:
#     for day in line:
#         day=day.centet(6)
#         print(day,end="  ")
#     print()
#
# import calendar
# result=calendar.month(19,9).splitlines()[2:]
# for line in result:
#     print(line)
# print(result)

import datetime


class Calendar:
    """
    以前类似实现日历功能
    1、返回列表嵌套列表的日历
    2、安装日历格式打印日历

    #如果一号周周一那么第一行1-7号   0
    # 如果一号周周二那么第一行empty*1+1-6号  1
    # 如果一号周周三那么第一行empty*2+1-5号  2
    # 如果一号周周四那么第一行empty*3+1-4号  3
    # 如果一号周周五那么第一行empyt*4+1-3号  4
    # 如果一号周周六那么第一行empty*5+1-2号  5
    #如果一号周日那么第一行empty*6+1号   6
    输入一月
    得到1月1日是周几
    []填充7个元素 索引0对应周一
    返回列表
    day_range 1-30
    """

    def __init__(self, month='now'):
        self.result = []

        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]

        # 获取当前月
        now = datetime.datetime.now()
        if month == 'now':
            month = now.month
            first_date = datetime.datetime(now.year, now.month, 1, 0, 0)
            # 年 月  日  时  分
        else:
            # assert int(month) in range (1,13)
            first_date = datetime.datetime(now.year, month, 1, 0, 0)

        if month in big_month:
            day_range = range(1, 32)  # 指定月份的总天数
        elif month in small_month:
            day_range = range(1, 31)
        else:
            day_range = range(1, 29)

        # 获取指定月份天数
        self.day_range = list(day_range)
        first_week = first_date.weekday()  # 获取指定月1号是周几  6

        line1 = []  # 第一行数据
        for e in range(first_week):
            line1.append('empty')
        for d in range(7 - first_week):
            line1.append(str(self.day_range.pop(0)))
        self.result.append(line1)
        while self.day_range:  # 如果总天数列表有值，接直接循环
            line = []  # 每个自列表
            for i in range(7):
                if len(line) < 7 and self.day_range:
                    line.append(str(self.day_range.pop(0)))
                else:
                    line.append('empty')
            self.result.append(line)

    def return_month(self):
        """
        返回列表嵌套列表的日历
        :return:
        """
        return self.result

    def print_month(self):
        """
        安装日历格式打印日历
        :return:
        """
        print("星期一  星期二  星期三  星期四  星期五  星期六  星期日")
        for line in self.result:
            for day in line:
                day = day.center(6)
                print(day, end="  ")
            print()


if __name__ == "__main__":
    c = Calendar()
    c.print_month()
    print(c.return_month())
