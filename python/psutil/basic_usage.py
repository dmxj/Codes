# -*- coding: utf-8 -* -
import psutil
'''
统计系统信息，参考：https://psutil.readthedocs.io/en/latest
'''
# ==================== CPU相关 ==============================

# 计算阻塞1秒的时间段内的占用，percpu为True返回列表，包含每一个CPU的占用，否则只有一个CPU占用的数值。默认为False
cpu_percent_list = psutil.cpu_percent(interval=1, percpu=True)
print("CPU占用百分比列表：", cpu_percent_list)

# 计算CPU的个数，当logical为False时，只统计物理CPU的个数，不统计逻辑CPU的个数。默认为True
cpu_num = psutil.cpu_count(logical=False)
print("CPU的个数（物理CPU）：",cpu_num)

# 计算CPU的统计数据
cpu_stats = psutil.cpu_stats()
print("自系统开机以来的上下文切换次数（包括主动与被动）:",cpu_stats.ctx_switches)
print("自系统开机以来的中断次数：",cpu_stats.interrupts)
print("自系统开机以来的软件的中断次数：",cpu_stats.soft_interrupts)
print("自系统开机以来的系统调用次数：",cpu_stats.syscalls)

# 计算CPU频率(包括当前值、最大值、最小值，使用Mhz作为单位)，percpu为True返回列表，默认为False
cpu_freq = psutil.cpu_freq(percpu=True)
print("CPU0 的频率的当前值: ",cpu_freq[0].current)
print("CPU0 的频率的最大值: ",cpu_freq[0].max)
print("CPU0 的频率的最小值: ",cpu_freq[0].min)


# ==================== 内存相关 ==============================

# 统计内存的相关使用（单位：字节bytes）
mem_stats = psutil.virtual_memory()
print("总的物理内存：",mem_stats.total)
print("在系统不进入内存交换的情况下，可立即分配给进程的内存：",mem_stats.available)
print("内存的使用量：",mem_stats.used)
print("没有被使用到的内存，这个变量并不能反应实际可使用的内存，使用available替换：",mem_stats.free)
print("当前使用或正在被使用的内存量（在RAM中）：",mem_stats.active)
print("标记为未使用的内存：",mem_stats.inactive)
# print("缓存，类似文件系统元信息等：",mem_stats.buffers)
# print("不同变量的缓存：",mem_stats.cached)
# print("可以同时由多个进程访问的共享内存：",mem_stats.shared)
# print("内核数据结构缓存：",mem_stats.slab)
print("被标记永远处于RAM中的内存，它永远不会移动到磁盘：",mem_stats.wired)

# 系统交换内存统计（单位：字节bytes）
mem_swap = psutil.swap_memory()
print("总的交换内存: ", mem_swap.total)
print("被使用的交换内存：", mem_swap.used)
print("未使用的交换内存：", mem_swap.free)
print("交换内存使用百分比[(total - available) / total * 100]：", mem_swap.percent)
print("累计被交换进入磁盘的内存量：", mem_swap.sin)
print("累计从磁盘交换出来的内存量：", mem_swap.sout)

# ==================== 磁盘相关 ==============================

# 统计系统磁盘分区情况（包括磁盘、挂载点、文件系统类型），参数all默认为False，此时将只返回系统磁盘的分区情况，否则全部返回
disk_part = psutil.disk_partitions()
for disk_item in disk_part:
    print("设备名称:{}, 挂载点:{}, 文件系统类型：{}".format(disk_item.device,disk_item.mountpoint,disk_item.fstype))

# 统计给定路径的磁盘使用量（包括总使用total、已使用used、未使用free、使用占比percent），单位：字节bytes
disk_usage = psutil.disk_usage("/")
print("/ 目录下的磁盘总使用量：",disk_usage.total)
print("/ 目录下的磁盘已使用量：",disk_usage.used)
print("/ 目录下的磁盘未使用量：",disk_usage.free)
print("/ 目录下的磁盘已使用占比（used/total）：",disk_usage.percent)

# 统计磁盘IO次数. 如果参数perdisk为True，则返回每一个物理磁盘的IO次数信息，默认为False，统计系统全局的IO次数；参数nowrap为True时，IO次数会累积，可以调用disk_io.clear()进行清除，默认为True
disk_io = psutil.disk_io_counters()
# disk_io.clear()
print("系统读磁盘的次数：",disk_io.read_count)
print("系统写磁盘的次数：",disk_io.write_count)
print("系统读磁盘的字节数：",disk_io.read_bytes)
print("系统写磁盘的字节数：",disk_io.write_bytes)
print("系统读磁盘使用的时间：",disk_io.read_time)
print("系统写磁盘使用的时间：",disk_io.write_time)
