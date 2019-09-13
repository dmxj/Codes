# -*- coding: utf-8 -* -
'''
使用命名管道进行不同进程的通信：服务端
参考：https://blog.csdn.net/mayao11/article/details/50618598
'''
import os
import time

# 服务端读的管道，客户端进程会往里写
read_path = "/tmp/server_in.pipe"

# 服务端写的管道，客户端会从里面读
write_path = "/tmp/server_out.pipe"

try:
    # 创建命名管道
    os.mkfifo(write_path)
    os.mkfifo(read_path)
except OSError as e:
    # 如果命名管道已经创建过了，那么无所谓
    print("mkfifo error:",e)

# 写入和读取的文件，正好好Client相反
rf = os.open(read_path,os.O_RDONLY)
wf = os.open(write_path,os.O_SYNC | os.O_CREAT | os.O_RDWR)

while True:
    # 接收请求
    s = os.read(rf,2)
    if len(s) == 0:
        # 没有收到字符，一般是唯一的发送方被关闭了。
        # 这里可以休息一下继续，对后续消息没有任何影响，也不会丢包。
        time.sleep(1)
        continue

    # 如果收到的字符串带一个s，打印出来
    # 用于调试和测试
    # if "z" in str(s):
    print("received", str(s))

    if str(s) == "exit":
        break

    # 在请求前面加一个s字母，返回
    os.write(wf, ("s%s" % str(s)).encode())

os.close(wf)
os.close(rf)
