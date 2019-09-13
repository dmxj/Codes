# -*- coding: utf-8 -* -
'''
通过图片减均值，对数据进行归一化
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

class ImgNormal(object):
    def __init__(self,img_path_list,img_size=0):
        self.img_path_list = img_path_list
        self.img_size = img_size
        self._load_images()

    def get_image_mean_and_show(self,is_show=False,save_path=None):
        mean_image = np.mean(self.resize_images,axis=0)
        resize_images = self.resize_images.copy()
        resize_images -= mean_image

        if is_show:
            plt.gcf().canvas.set_window_title('sub image mean')
            img_cnt = len(resize_images)
            for i,img in enumerate(np.vstack([self.resize_images, resize_images]).tolist()):
                plt.subplot(2,img_cnt,i+1)
                plt.imshow(img)
                plt.xticks([])
                plt.yticks([])
            plt.show()

        if save_path is not None:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            img_cnt = len(resize_images)
            for i in range(img_cnt):
                save_name = os.path.join(save_path,os.path.basename(self.img_path_list[i]))
                cv2.imwrite(save_name,resize_images[i,:,:,:])

        return resize_images

    def get_pixel_mean_and_show(self,is_show=False,save_path=None):
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for image in self.images:
            sum_r += image[:,:,0].mean()
            sum_g += image[:,:,1].mean()
            sum_b += image[:,:,2].mean()
        img_cnt = len(self.images)
        img_mean = [sum_r/img_cnt,sum_g/img_cnt,sum_b/img_cnt]
        images = self.images.copy()
        for i in range(img_cnt):
            images[i] = images[i].astype(np.float64)
            images[i] -= img_mean

        if is_show:
            for i,img in enumerate(self.images + images):
                plt.subplot(2,img_cnt,i+1)
                plt.imshow(img)
                plt.xticks([])
                plt.yticks([])
            plt.show()

        if save_path is not None:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            for i in range(img_cnt):
                save_name = os.path.join(save_path,os.path.basename(self.img_path_list[i]))
                cv2.imwrite(save_name,images[i])

        return images

    def _load_images(self):
        self.images = []
        self.resize_images = []
        self.total_size = 0
        for img_path in self.img_path_list:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.images.append(img)
            self.total_size += (img.shape[0] + img.shape[1])
            if self.img_size > 0:
                img_resize = cv2.resize(img,(self.img_size,self.img_size))
                self.resize_images.append(img_resize)
        if self.img_size == 0:
            self.img_size = self.total_size//(len(self.images)*2)
            for img in self.images:
                img_resize = cv2.resize(img, (self.img_size, self.img_size))
                self.resize_images.append(img_resize)

        self.resize_images = np.array(self.resize_images,dtype=np.float64)

if __name__ == "__main__":
    img_list = glob.glob("imgs/*")
    imgNormal = ImgNormal(img_list)

    # imgNormal.get_image_mean_and_show(True,"./imgs_sub_img_mean/")
    imgNormal.get_pixel_mean_and_show(True,"./imgs_sub_pixel_mean/")

