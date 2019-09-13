# -*- coding: utf-8 -* -
'''
两张图片拼接成一张图片
'''
import cv2
import numpy as np

img_file_lists = ["imgs/img0.jpg","imgs/img1.jpg"]

def cat_imgs():
    ims = [cv2.imread(img_file) for img_file in img_file_lists]
    im_sizes = [(im.shape[0],im.shape[1]) for im in ims]

    total_height = sum([h for h,w in im_sizes])
    max_height = max([h for h,w in im_sizes])
    total_width = sum([w for h,w in im_sizes])
    max_width = max([w for h,w in im_sizes])

    # 创建背景画布
    image = np.zeros((max_height,total_width,3),np.uint8)
    # 白色画布
    image.fill(255)

    x = 0
    for im in ims:
        h,w,_ = im.shape
        image[0:h,x:x+w,:] = im
        x+=w

    cv2.imshow("concat_img",image)
    cv2.imwrite("imgs/concat_img.jpg",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cat_imgs()


