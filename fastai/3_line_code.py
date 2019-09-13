# -*- coding: utf-8 -* -
'''
三行代码展示fastai的威力
来自：https://becominghuman.ai/3-lines-of-code-deciphering-fast-ai-658e79151af8
'''

'''
# 定义数据的转换或预处理方式。
- arch：预训练的网络架构或者将要使用的模型；
- sz: 输入图片的尺寸；
- aug_tfms: 数据变换函数；
- max_zoom：随机最大放大1.2倍
tfms = tfms_from_model(arch,sz,aug_tfms=trainsforms_side_on,max_zoom=1.2)

# 定义数据
- path：图片的路径；
- labels_csv：标注的csv文件；
- val_idxs：用于验证集的id列表；
- test_name：
- suffix：合法的文件后缀；
- tfms：上一步定义的数据转换；
- bs：batch_size
data = ImageClassifierData.from_csv(path, "train", labels_csv, val_idxs=val_idxs, test_name="test", suffix=".jpg",tfms=tfms,bs=bs)

# 定义模型训练器
- arch：再次传入预训练的网络架构或者将要使用的模型；
- data：训练数据；
- precompute：是否使用预训练的激活权重来初始化，True的时候将不会发生数据增广；
- ps: dropout参数
learn = ConvLearner.pretrained(arch, data, precompute=True, ps=0.5)

'''





