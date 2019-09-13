# -*- coding: utf-8 -* -
'''
使用Pytorch的dataloader加载mnist数据集
'''
import os
import torch
from torchvision import datasets, transforms

batch_size = 1000
dataset_path = "/Users/rensike/Resources/datasets/pytorch"

'''构建'''
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST(root=os.path.join(dataset_path,"mnist"), train=True, download=True, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])),
    batch_size=batch_size,
    shuffle=True)
test_loader = torch.utils.data.DataLoader(
    datasets.MNIST(root=os.path.join(dataset_path,"mnist"), train=False, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])),
    batch_size=batch_size,
    shuffle=True)

print("训练集的数据总数：",len(train_loader.dataset))
print("测试集的数据总数：",len(test_loader.dataset))
print("训练集的batch个数：",len(train_loader))
print("测试集的batch个数：",len(test_loader))

for batch, (data, target) in enumerate(train_loader):
    print("【训练集】batch:{},data.shape:{},target.shape:{}".format(batch,data.shape,target.shape))

for batch, (data, target) in enumerate(test_loader):
    print("【测试】batch:{},data.shape:{},target.shape:{}".format(batch,data.shape,target.shape))