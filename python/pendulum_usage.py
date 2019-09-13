# -*- coding: utf-8 -* -
'''
使用pendulum更简易地操作时间。参考：https://github.com/sdispater/pendulum
pip install pendulum
'''
import pendulum

# 查看当前时间，通过填充tz参数，指定时区，默认不填为本地时间
now_time = pendulum.now()
print("现在的时间是：",now_time)

# 转换时区
now_in_paris = now_time.in_timezone("Europe/Paris")
print("巴黎时间是：",now_in_paris)

# 明天
tomorrow = pendulum.now().add(days=1)
print("明天的现在：", tomorrow)

# 一周前
last_week = pendulum.now().subtract(weeks=1)
print("下周的现在：", last_week)

# 两分钟之前
past = pendulum.now().subtract(minutes=2)
print("两分钟之前：", past)
print("两分钟之前的时间和现在的时间差距，用人话描述：", past.diff_for_humans())

# 时间差
delta = past - last_week
print("两分钟前和上一周的时间差：",delta)
print("两分钟前和上一周的时间差，用人话描述：",delta.in_words())
print("两分钟前和上一周的时间差, 天数：",delta.days)
print("两分钟前和上一周的时间差, 小时数：",delta.hours)

# 定义时间
dt = pendulum.datetime(2013, 3, 31, 2, 30, tz='Europe/Paris')
print("巴黎时间：",dt)





