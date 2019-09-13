# -*- coding: utf-8 -* -
'''
mmcv创建进度条
参考：https://mmcv.readthedocs.io/en/latest/utils.html#progressbar
'''
import mmcv
import time
def do_task(i):
    time.sleep(1)
    return i + 1

'''
依次调用task，输出进度
'''
tasks = list(range(10))
results = mmcv.track_progress(do_task,tasks)
print(results)

'''
多进程执行task，8个进程
'''
results = mmcv.track_parallel_progress(do_task,tasks,8)
print(results)
