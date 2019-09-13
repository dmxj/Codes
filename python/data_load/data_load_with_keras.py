# -*- coding: utf-8 -* -
'''
使用Keras加载数据集
- boston_housing 波士顿房价回归数据集
- mnist 手写字体分类图像数据集
- cifar10 图像分类数据集
- cifar100 图像分类数据集
- fashion_mnist 图像分类数据集
- imdb IMDB 情感分类文本数据集
- reuters 路透社主题分类文本数据集
'''
from tensorflow.keras import datasets
import os

datasets_prefix = "/Users/rensike/Resources/datasets/keras"

'''波士顿房价数据集'''
(boston_housing_x_train, boston_housing_y_train), (boston_housing_x_test, boston_housing_y_test) = datasets.boston_housing.load_data(
    os.path.join(datasets_prefix, "boston_housing.npz"))
print("波士顿房价数据集，训练集X shape:", boston_housing_x_train.shape)     # (404, 13)
print("波士顿房价数据集，训练集Y shape:", boston_housing_y_train.shape)     # (404,)
print("波士顿房价数据集，测试集X shape:", boston_housing_x_test.shape)      # (102, 13)
print("波士顿房价数据集，测试集Y shape:", boston_housing_y_test.shape)      # (102,)

'''手写字体数据集'''
(mnist_x_train, mnist_y_train), (mnist_x_test, mnist_y_test) = datasets.mnist.load_data(
    os.path.join(datasets_prefix, "mnist.npz"))
print("手写字体数据集，训练集X shape:", mnist_x_train.shape)       # (60000, 28, 28)
print("手写字体数据集，训练集Y shape:", mnist_y_train.shape)       # (60000,)
print("手写字体数据集，测试集X shape:", mnist_x_test.shape)        # (10000, 28, 28)
print("手写字体数据集，测试集Y shape:", mnist_y_test.shape)        # (10000,)

'''cifar10数据集'''
(cifar10_x_train, cifar10_y_train), (cifar10_x_test, cifar10_y_test) = datasets.cifar10.load_data()
print("cifar10数据集，训练集X shape:", cifar10_x_train.shape)     # (50000, 32, 32, 3)
print("cifar10数据集，训练集Y shape:", cifar10_y_train.shape)     # (50000, 1)
print("cifar10数据集，测试集X shape:", cifar10_x_test.shape)      # (10000, 32, 32, 3)
print("cifar10数据集，测试集Y shape:", cifar10_y_test.shape)      # (10000, 1)

'''cifar100数据集'''
(cifar100_x_train, cifar100_y_train), (cifar100_x_test, cifar100_y_test) = datasets.cifar100.load_data()
print("cifar100数据集，训练集X shape:", cifar100_x_train.shape)    # (50000, 32, 32, 3)
print("cifar100数据集，训练集Y shape:", cifar100_y_train.shape)    # (50000, 1)
print("cifar100数据集，测试集X shape:", cifar100_x_test.shape)     # (10000, 32, 32, 3)
print("cifar100数据集，测试集Y shape:", cifar100_y_test.shape)     # (10000, 1)

'''imdb情感分类数据集'''
(imdb_x_train, imdb_y_train), (imdb_x_test, imdb_y_test) = datasets.imdb.load_data(
    path=os.path.join(datasets_prefix, "imdb.npz"))
print("imdb情感分类数据集，训练集X shape:", imdb_x_train.shape)        # (25000,)
print("imdb情感分类数据集，训练集Y shape:", imdb_y_train.shape)        # (25000,)
print("imdb情感分类数据集，测试集X shape:", imdb_x_test.shape)        # (25000,)
print("imdb情感分类数据集，测试集Y shape:", imdb_y_test.shape)        # (25000,)

'''reuters主题分类数据集'''
(reuters_x_train, reuters_y_train), (reuters_x_test, reuters_y_test) = datasets.reuters.load_data(
    path=os.path.join(datasets_prefix, "reuters.npz"))
print("reuters主题分类数据集，训练集X shape:", reuters_x_train.shape)  # (8982,)
print("reuters主题分类数据集，训练集Y shape:", reuters_y_train.shape)  # (8982,)
print("reuters主题分类数据集，测试集X shape:", reuters_x_test.shape)   # (2246,)
print("reuters主题分类数据集，测试集Y shape:", reuters_y_test.shape)   # (2246,)
