# -*- coding: utf-8 -* -
'''
使用easydict更简单地操作字典
pip install easydict
'''
from easydict import EasyDict as edict

d = edict({"foo":3,'bar':{"x":1,"y":2}})
print(d.foo)
print(d.bar.x)

y = edict(foo=3)
print(y.foo)
print(y["foo"])

z = edict(log=False)
z.debug = True
print(z.items())
