# -*- coding: utf-8 -* -
import psutil
'''
统计当前进程的资源使用
'''
import psutil

process_info = psutil.Process()

# 获取当前进程的CPU利用率
cpu_precent = process_info.cpu_percent()
print("当前进程的CPU占用情况：",cpu_precent)

# 获取当前进程的线程数量
num_threads = process_info.num_threads()
print("当前进程的线程数量：",num_threads)

# 获取进程的内存使用情况
mem_info = process_info.memory_info()
print("当前进程的占用的物理内存大小：",mem_info.rss)
print("当前进程的占用的虚拟内存大小：",mem_info.vms)

mem_precent = process_info.memory_percent()
print("当前进程的使用内存占比：",mem_precent)

# 获取进程的磁盘空间占用情况
print("/ 路径下当前进程使用的磁盘空间：",psutil.disk_usage('/').used)
print("/ 路径下当前进程没有使用的磁盘空间：",psutil.disk_usage('/').free)
print("/ 路径下当前进程使用的磁盘空间百分比：",psutil.disk_usage('/').percent)



