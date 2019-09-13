# -*- coding: utf-8 -* -
'''
使用wget库下载文件，参考：https://pypi.org/project/wget/
pip install wget
'''
import wget
url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
filename = wget.download(url,out="./result/")
print(filename)

