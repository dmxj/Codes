# -*- coding: utf-8 -* -
'''
使用MMCV读取文本文件到list或dict中
参考：https://mmcv.readthedocs.io/en/latest/io.html#load-a-text-file-as-a-list-or-dict
'''
import mmcv

'''读取文件的每一行放到一个列表中'''
ll = mmcv.list_from_file("a.txt")
print(ll)

'''读取文件的每一行，跳过2行，从第3行开始'''
ll = mmcv.list_from_file("a.txt",offset=2)
print(ll)

'''读取文件的每一行，最多读取2行'''
ll = mmcv.list_from_file("a.txt",max_num=2)
print(ll)

'''读取文件的每一行，是保存以hello开头的文本'''
ll = mmcv.list_from_file("a.txt",prefix="hello")
print(ll)

'''将文本文件读取到一个字典中，文本文件每一行以空格分割，第一个作为键，后面的作为值'''
dt = mmcv.dict_from_file("b.txt")
print(dt)