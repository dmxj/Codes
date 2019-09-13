# -*- coding: utf-8 -* -
'''
使用fast ai进行数据增广
'''
'''
五个步骤避免过拟合：
获取更多数据、数据增广、generalized architectures、正则化、降低网络复杂度
'''
'''
fastai中有三种基本的变化：transforms_basic, transforms_side_on 和 transforms_top_down，这三种变化由fastai源码中的transforms.py中的三个独立的类定义。
transforms_basic包括RandomRotate、RandomLighting；
transforms_side_on包括transforms_basic、RandomFlip；
transforms_top_down包括transforms_basic、RandomDihedral
'''
from matplotlib.pyplot import plot
import fastai
from fastai import vision

im = vision.open_image("cluo.jpg")
im.show(figsize=(10,5))
