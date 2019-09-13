# -*- coding: utf-8 -* -
'''
使用cifar10数据集进行训练
'''

from fastai import *
from fastai.vision import *
from fastai.vision.models.wrn import wrn_22

torch.backends.cudnn.benchmark = True

# fastai下载数据集有问题，此处直接指定下载好的文件的路径
# path = untar_data(URLs.CIFAR)
path = "/Users/rensike/Resources/datasets/fastai/cifar10"

ds_tfms = ([*rand_pad(4, 32), flip_lr(p=0.5)], [])
data = ImageDataBunch.from_folder(path, valid='test', ds_tfms=ds_tfms, bs=512).normalize(cifar_stats)

print("第一次训练开始")
# CPU环境下不支持fp16
# learn = Learner(data, wrn_22(), metrics=accuracy).to_fp16()
learn = Learner(data, wrn_22(), metrics=accuracy)
learn.fit_one_cycle(30, 3e-3, wd=0.4, div_factor=10, pct_start=0.5)
print("第一次训练结束，准确率:{}".format(accuracy(*learn.get_preds())))

print("第二次训练开始")
# CPU环境下不支持fp16
# learn = Learner(data, wrn_22(), metrics=accuracy).to_fp16().mixup()
learn = Learner(data, wrn_22(), metrics=accuracy).mixup()
learn.fit_one_cycle(24, 3e-3, wd=0.2, div_factor=10, pct_start=0.5)
print("第二次训练结束，准确率:{}".format(accuracy(*learn.get_preds())))

