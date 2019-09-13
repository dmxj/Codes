# -*- coding: utf-8 -* -
'''
使用Pytorch加载数据集
'''
from torchvision import datasets
import os

dataset_path = "/Users/rensike/Resources/datasets/pytorch"

'''加载手写字体识别数据集'''
mnist_train = datasets.MNIST(root=os.path.join(dataset_path,"mnist"),train=True,download=True)
mnist_train_data,mnist_train_label = mnist_train.data,mnist_train.targets
mnist_test = datasets.MNIST(root=os.path.join(dataset_path,"mnist"),train=False,download=True)
mnist_test_data,mnist_test_label = mnist_test.data,mnist_test.targets
print("手写字体数据集，train data shape:",mnist_train_data.shape)   # [60000, 28, 28]
print("手写字体数据集，train label shape:",mnist_train_label.shape) # [60000]
print("手写字体数据集，test data shape:",mnist_test_data.shape)     # [10000, 28, 28]
print("手写字体数据集，test label shape:",mnist_test_label.shape)    # [10000]

'''cifar10数据集'''
cifar10_train = datasets.CIFAR10(root=os.path.join(dataset_path,"cifar10"),train=True,download=True)
cifar10_test = datasets.CIFAR10(root=os.path.join(dataset_path,"cifar10"),train=False,download=True)
print("cifar10数据集，train data shape:",cifar10_train.data.shape)          # (50000, 32, 32, 3)
print("cifar10数据集，train label length:",len(cifar10_train.targets))      # 50000
print("cifar10数据集，test data shape:",cifar10_test.data.shape)            # (10000, 32, 32, 3)
print("cifar10数据集，test label length:",len(cifar10_test.targets))        # 10000

'''cifar100数据集'''
cifar100_train = datasets.CIFAR100(root=os.path.join(dataset_path,"cifar100"),train=True,download=True)
cifar100_test = datasets.CIFAR100(root=os.path.join(dataset_path,"cifar100"),train=False,download=True)
print("cifar100数据集，train data shape:",cifar100_train.data.shape)        # (50000, 32, 32, 3)
print("cifar100数据集，train label length:",len(cifar100_train.targets))    # 50000
print("cifar100数据集，test data shape:",cifar100_test.data.shape)          # (10000, 32, 32, 3)
print("cifar100数据集，test label length:",len(cifar100_test.targets))      # 10000

'''fashion mnist数据集'''
fashion_mnist_train = datasets.FashionMNIST(root=os.path.join(dataset_path,"fashion_mnist"),train=True,download=True)
fashion_mnist_test = datasets.FashionMNIST(root=os.path.join(dataset_path,"fashion_mnist"),train=False,download=True)
print("fashion mnist数据集，train data shape:",fashion_mnist_train.data.shape)
print("fashion mnist数据集，train label shape:",fashion_mnist_train.targets.shape)
print("fashion mnist数据集，test data shape:",fashion_mnist_test.data.shape)
print("fashion mnist数据集，test label shape:",fashion_mnist_test.targets.shape)

'''svhn数据集(街景门牌号数据集)'''
svhn_train = datasets.SVHN(root=os.path.join(dataset_path,"svhn"),split="train",download=True)
svhn_test = datasets.SVHN(root=os.path.join(dataset_path,"svhn"),split="test",download=True)
svhn_extra = datasets.SVHN(root=os.path.join(dataset_path,"svhn"),split="extra",download=True)
print("svhn数据集，train data shape:",svhn_train.data.shape)
print("svhn数据集，train label shape:",svhn_train.labels.shape)
print("svhn数据集，test data shape:",svhn_test.data.shape)
print("svhn数据集，test label shape:",svhn_test.data.shape)
print("svhn数据集，extra data shape:",svhn_extra.data.shape)
print("svhn数据集，extra label shape:",svhn_extra.data.shape)

'''Semeion手写字体识别数据集'''
semeion = datasets.SEMEION(root=os.path.join(dataset_path,"semeion"),download=True)
print("Semeion数据集，data shape:",semeion.data.shape)
print("Semeion数据集，labels shape:",semeion.labels.shape)

'''STL10图像分类数据集'''
'''STL10包括500个训练数据、100000个未标注数据，图像是96X96像素，共10类：airplane, bird, car, cat, deer, dog, horse, monkey, ship, truck'''
stl10_train = datasets.STL10(root=os.path.join(dataset_path,"stl10"),split="train",download=True)
stl10_test = datasets.STL10(root=os.path.join(dataset_path,"stl10"),split="test",download=True)
stl10_unlabeled = datasets.STL10(root=os.path.join(dataset_path,"stl10"),split="unlabeled",download=True)
print("STL10数据集，train data shape:",stl10_train.data.shape)
print("STL10数据集，train labels shape:",stl10_train.labels.shape)
print("STL10数据集，test data shape:",stl10_test.data.shape)
print("STL10数据集，test labels shape:",stl10_test.labels.shape)
print("STL10数据集，unlabeled data shape:",stl10_unlabeled.data.shape)
print("STL10数据集，unlabeled labels shape:",stl10_unlabeled.labels.shape)

'''PhotoTour数据集'''
phototour_train = datasets.PhotoTour(root=os.path.join(dataset_path,"phototour"),name="phototour_train",train=True,download=True)
phototour_test = datasets.PhotoTour(root=os.path.join(dataset_path,"phototour"),name="phototour_test",train=False,download=True)
print("PhotoTour数据集，train data shape:",phototour_train.data.shape)
print("PhotoTour数据集，train labels shape:",phototour_train.labels.shape)
print("PhotoTour数据集，train matches shape:",phototour_train.matches.shape)
print("PhotoTour数据集，test data shape:",phototour_test.data.shape)
print("PhotoTour数据集，test labels shape:",phototour_test.labels.shape)
print("PhotoTour数据集，test matches shape:",phototour_test.matches.shape)







