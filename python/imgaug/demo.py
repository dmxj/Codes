# -*- coding: utf-8 -* -
"""
示例
"""
import cv2
from imgaug import augmenters as iaa
import matplotlib.pyplot as plt


if __name__ == '__main__':
    image_file = "/Users/rensike/Work/昆山立讯耳机/pascal_voc_data/JPEGImages/ng_划伤1222715.png"
    img = cv2.imread(image_file)

    aug_seq = iaa.Sequential([
        iaa.ContrastNormalization((0.75, 1.5)),
        iaa.Multiply((0.75, 1.5)),
        iaa.AddToHueAndSaturation((-20, 20)),
    ])

    aug_img = aug_seq.augment_image(img)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(img)
    plt.subplot(2, 1, 2)
    plt.imshow(aug_img)
    plt.show()



