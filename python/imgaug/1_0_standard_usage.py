# -*- coding: utf-8 -* -
"""
标准的用法
"""
from imgaug import augmenters as iaa

# 加载批次数据
def load_batch(batch_idx):
    pass

# 训练模型
def train_on_images(images):
    pass

seq = iaa.Sequential([
    iaa.Crop(px=(0,16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0,3.0)) # blur images with a sigma of 0 to 3.0
])

for batch_idx in range(1000):
    # 'images' should be either a 4D numpy array of shape (N, height, width, channels)
    # or a list of 3D numpy arrays, each having shape (height, width, channels).
    # Grayscale images must have shape (height, width, 1) each.
    # All images must have numpy's dtype uint8. Values are expected to be in
    # range 0-255.
    images = load_batch(batch_idx)
    images_aug = seq.augment_images(images)
    train_on_images(images_aug)


