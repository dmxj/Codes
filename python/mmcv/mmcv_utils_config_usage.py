# -*- coding: utf-8 -* -
'''
使用MMCV读取配置文件
参考：https://mmcv.readthedocs.io/en/latest/utils.html#config
'''
from mmcv import Config

cfg = Config.fromfile("config.py")
assert cfg.a == 1
assert cfg.b.b1 == [0,1,2]
cfg.c = None
assert cfg.c == None
