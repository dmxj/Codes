# -*- coding: utf-8 -* -
from PIL import Image
import numpy as np


def pil_img_to_np_arr(im):
    '''
    将Pillow图像转换为numpy数组
    :param im: Pillow图像
    :return:
    '''
    img_arr = np.array(im)
    return img_arr


def np_arr_to_pil(arr):
    '''
    将numpy数组转换为Pillow图像
    :param arr: numpy 数组
    :return:
    '''
    im = Image.fromarray(arr.astype('uint8')).convert('RGB')
    return im


if __name__ == "__main__":
    im = Image.open("cluo.jpg")
    img_arr = pil_img_to_np_arr(im)
    img_recover = np_arr_to_pil(img_arr)