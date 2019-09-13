# -*- coding: utf-8 -* -
'''
使用colorama，让打印带颜色
pip install colorama
'''
import colorama

print(colorama.Fore.RED, "这段打印出的文字是红色")
print(colorama.Fore.BLUE, "这段打印出的文字是蓝色")
print(colorama.Fore.GREEN, "这段打印出的文字是绿色")

print(colorama.Back.YELLOW, "这行背景是黄色")

