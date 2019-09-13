# -*- coding: utf-8 -* -
'''
两张图片合成一张图片
'''
import cv2

img1 = cv2.imread('imgs/img0.jpg')
img2 = cv2.imread('imgs/img1.jpg')

h, w, _ = img1.shape
img2 = cv2.resize(img2, (w,h), interpolation=cv2.INTER_AREA)

'''合并两张图片，要求两张图片必须是同样的size'''
img_mix = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img_mix', img_mix)

cv2.imwrite("imgs/img_mix.jpg",img_mix)

cv2.waitKey(0)
cv2.destroyAllWindows()
