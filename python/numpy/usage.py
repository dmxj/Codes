# -*- coding: utf-8 -* -
"""
numpy的使用方法
"""
import numpy as np

# 从0-1等间隔产生5个数，包括0和1（0, 0.25, 0.5, 0.75, 1）
np.linspace(0,1,5)

# 扩展数组的shape
arr = np.arange(0,10)
print(arr.shape)
# 以下两种写法等价
arr2 = np.expand_dims(arr,axis=0)
print(arr2.shape)
arr2 = arr[np.newaxis,:]
print(arr2.shape)

# 重复数组
arr = np.array([1,2])
np.tile(arr,3) # output: [1,2,1,2,1,2]
np.tile(arr,(2,2)) # output: [[1,2,1,2],[1,2,1,2]]