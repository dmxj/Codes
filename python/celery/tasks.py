# -*- coding: utf-8 -* -
'''
定义了矩阵相加、矩阵相乘、矩阵相减三个task
启动：celery -A tasks worker --loglevel=info
'''
import numpy as np
from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def add(arr_1,arr_2):
    return np.add(arr_1,arr_2)

@app.task
def mul(arr_1,arr_2):
    return np.matmul(arr_1,arr_2)

@app.task
def sub(arr_1,arr_2):
    return np.subtract(arr_1,arr_2)
