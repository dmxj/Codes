# -*- coding: utf-8 -* -
'''
MMCV读取并转换颜色空间
参考：https://mmcv.readthedocs.io/en/latest/image.html#color-space-conversion
'''
import mmcv
img = mmcv.imread("cluo.jpg")
img1 = mmcv.bgr2rgb(img)
img2 = mmcv.bgr2gray(img)
img3 = mmcv.bgr2gray(img)

