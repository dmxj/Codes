# -*- coding: utf-8 -* -
'''
时间日期相关
'''
import time
import datetime

# 获取当前的时间
dt1 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
dt2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

print(time.strftime("%Y%m%d-%H:%M", time.localtime(time.time())))