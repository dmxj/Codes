# -*- coding: utf-8 -* -
'''
手写字体识别训练
'''
import fastai
from fastai import vision

'''
下载手写字体数据集，数据集URL、文件名称、保存路径（这里下载不下来，只能手动先下载解压好，直接传路径了）
'''
# path = fastai.untar_data(fastai.URLs.MNIST_SAMPLE)
path = "/Users/rensike/Resources/datasets/fastai/mnist_sample"
'''
构建数据集，数据路径、数据预处理方式、bach_size
'''
data = vision.ImageDataBunch.from_folder(path, ds_tfms=(vision.rand_pad(2, 28), []),
                                         bs=64)
'''
数据归一化
'''
data.normalize(vision.imagenet_stats)
'''
显示数据集中的第一个数据
'''
img, label = data.train_ds[0]
print(label)
img.show()

'''
创建一个学习器。数据集、模型类型、评估指标
'''
learn = vision.create_cnn(data, vision.models.resnet18, metrics=fastai.vision.accuracy)
'''
训练1个epoch，学习率0.01
'''
learn.fit(1, 0.01)
'''
打印：
epoch     train_loss  valid_loss  accuracy
1         0.062133    0.008120    0.997056
'''

'''
打印训练完的模型的准确率
'''
acc = fastai.vision.accuracy(*learn.get_preds())
print(acc)
