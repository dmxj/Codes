# -*- coding: utf-8 -* -
'''
使用mmcv计算程序运行时间
参考：https://mmcv.readthedocs.io/en/latest/utils.html#timer
'''
import time
import mmcv

timer = mmcv.Timer()
time.sleep(1)
print(timer.since_start())  # 打印第一次定义timer到这里，代码共执行的时间
time.sleep(2)
print(timer.since_last_check()) # 打印从上一次执行since_start到这里，代码共执行的时间
print(timer.since_start())




