# -*- coding: utf-8 -* -
'''
调用tasks启动的进程服务
'''
from python.celery import tasks
from kombu import Queue,Exchange

if __name__ == '__main__':
    import numpy as np
    arr1 = np.random.rand(100,100)
    arr2 = np.random.rand(100,100)

    add_res = tasks.add.apply_async((arr1,arr2))

    mul_res = tasks.mul.apply_async((arr1,arr2))

    sub_res = tasks.sub.apply_async((arr1,arr2))

    print("add_res shape:",add_res.get().shape)
    print("mul_res shape:",mul_res.get().shape)
    print("sub_res shape:",sub_res.get().shape)


