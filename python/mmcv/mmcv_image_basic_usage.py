# -*- coding: utf-8 -* -
'''
使用MMCV读、写图片文件
'''
import mmcv
import numpy as np

'''读取图片，3通道'''
img = mmcv.imread("cluo.jpg")
'''读取图片，灰度图片'''
img_gray = mmcv.imread("cluo.jpg",flag="grayscale")
'''从已有图片对象复制出一个图片对象'''
img_ = mmcv.imread(img)

'''图片保存到本地'''
mmcv.imwrite(img,"cluo_out.jpg")

'''从文件字节中读取图片'''
with open("cluo.jpg","rb") as f:
    data = f.read()
img = mmcv.imfrombytes(data)

'''显示图片'''
mmcv.imshow("cluo.jpg")

for i in range(10):
    img = np.random.randint(256,size=(100,100,3),dtype=np.uint8)
    mmcv.imshow(img,win_name="test image",wait_time=200)

