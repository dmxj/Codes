# -*- coding: utf-8 -* -
'''
fuzzywuzzy是一个简单好用的字符串模糊匹配的库
pip install fuzzywuzzy
'''
from fuzzywuzzy import fuzz

# 计算相似度
r1 = fuzz.ratio("Hit me with your best shot", "Hit me with your pet shark")
print("以上两个句子的相似度是：", r1)

# 部分匹配相似度
r2 = fuzz.partial_ratio("this is a test", "this is a test!")
print("以上两个句子的相似度，部分相似度：", r2)

