# -*- coding: utf-8 -* -
'''
MMCV显示图片相关
参考：https://mmcv.readthedocs.io/en/latest/visualization.html
'''
import mmcv
import numpy as np

# 显示图片文件
mmcv.imshow("cluo.jpg")

# 显示numpy数组格式的图片
img = np.random.rand(100,100,3)*255
mmcv.imshow(img)

# 显示图片并伴有bounding box
img = np.random.rand(100,100,3)*255
bboxes = np.array([[0,0,50,50],[20,20,60,60]])
mmcv.imshow_bboxes(img,bboxes,colors=["red"],show=False,out_file="cluo_bbox.jpg")

# 显示图片并伴有bounding box以及框的标题
labels = np.array([1,3])
classes = ["类别0","类别1","类别2","类别3"]
mmcv.imshow_det_bboxes(img,bboxes,labels,classes,bbox_color="green",text_color="blue",out_file="cluo_bbox_label.jpg")

