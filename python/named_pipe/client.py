# -*- coding: utf-8 -* -
'''
使用命名管道进行不同进程的通信：客户端
参考：https://blog.csdn.net/mayao11/article/details/50618598
'''
import os
import time

# 服务端进程读的pipe，客户端进程往里写
write_path = "/tmp/server_in.pipe"
# 服务端进程写的pipe，客户端进程进行读
read_path = "/tmp/server_out.pipe"

couter = 1

wf = os.open(write_path,os.O_SYNC | os.O_CREAT | os.O_RDWR)
print("Client open wf:",wf)

rf = None

while True:
    # Client不断发送请求，即往管道中写数据
    req = "%s "%couter
    len_send = os.write(wf,req.encode())
    print("request ",req,len_send)

    couter += 1

    if rf is None:
        # *要点1：在这里第一次打开read_path，实际这里的open是一个阻塞操作
        # 打开的时机很重要。如果在程序刚开始，没发送请求就打开read_path，肯定会阻塞住
        rf = os.open(read_path,os.O_RDONLY)
        print("Client open rf:",rf)

    # 接收Server回应
    s = os.read(rf,1024)
    if len(s) == 0:
        # 一般来说，是管道被意外关闭了，比如Server退出了
        break

    print("received:",str(s))

    # 这个例子里没有sleep，客户端以最高速度发送数据，可以观察执行效果

os.close(rf)
os.close(wf)



