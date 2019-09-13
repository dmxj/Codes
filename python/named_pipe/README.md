## 命名管道示例说明
参考：https://blog.csdn.net/mayao11/article/details/50618598
```angular2html
这个例子具有一定实用性：
1、无论先执行Server.py还是Client.py都可以正常工作。
2、Server.py与Client.py执行时，可以在另一个控制台里输入   echo zzzzz > /tmp/server_in.pipe，可以观察到，server可以同时处理多个来源的请求
3、实际上在进程交互时，每个进程既是一个Client又是一个Server，每个进程只有一个用于接收别人请求的pipe，然后接收请求后把处理结果返回给发送方的pipe。这样网络就联系起来了。和匿名管道的架构是一致的。
```
