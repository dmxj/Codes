# -*- coding: utf-8 -* -
'''
使用progressbar打印进度条
pip install progressbar
'''
from progressbar import ProgressBar
import time

if __name__ == "__main__":
    pbar = ProgressBar(maxval=10)
    for i in range(10):
        pbar.update(i+1)
        time.sleep(1)
    pbar.finish()

# 输出：
'''
40% (4 of 10) |##########               | Elapsed Time: 0:00:03 ETA:   0:00:06
'''


