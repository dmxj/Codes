# -*- coding: utf-8 -* -
'''
统计系统信息
'''
import pynvml
import psutil
import simplejson as json
import time
from threading_timer import Timer


def format_bytes(bytes):
    if bytes < 1024:  # 比特
        bytes = str(round(bytes, 2)) + ' B'  # 字节
    elif bytes >= 1024 and bytes < 1024 * 1024:
        bytes = str(round(bytes / 1024, 2)) + ' KB'  # 千字节
    elif bytes >= 1024 * 1024 and bytes < 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024, 2)) + ' MB'  # 兆字节
    elif bytes >= 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024, 2)) + ' GB'  # 千兆字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024, 2)) + ' TB'  # 太字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' PB'  # 拍字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' EB'  # 艾字节
    return bytes


def get_system_metrics():
    '''
    获取系统资源
    :return:
    '''
    metrics = {}
    # CPU占用率
    cpu_percent = psutil.cpu_percent()
    metrics["CPU"] = "{}%".format(cpu_percent)
    # 内存使用率
    mem_stats = psutil.virtual_memory()
    mem_used = mem_stats.used
    mem_total = mem_stats.total
    mem_percent = str(round(mem_used * 1.0 / mem_total * 100, 2)) + "%"
    metrics["Mem"] = mem_percent
    metrics["MemUsed"] = format_bytes(mem_used)
    metrics["MemAvail"] = format_bytes(mem_total - mem_used)

    try:
        pynvml.nvmlInit()
        deviceCount = pynvml.nvmlDeviceGetCount()
        for i in range(deviceCount):
            gpu_key = "GPU" + str(i)
            metrics[gpu_key] = {}
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
            util_rate = pynvml.nvmlDeviceGetUtilizationRates(handle)

            gpu_mem_used = meminfo.used
            gpu_mem_total = meminfo.total
            gpu_mem_avail = gpu_mem_total - gpu_mem_used

            metrics[gpu_key]["Mem"] = str(util_rate.memory) + "%"
            metrics[gpu_key]["MemUsed"] = format_bytes(gpu_mem_used)
            metrics[gpu_key]["MemAvail"] = format_bytes(gpu_mem_avail)
            metrics[gpu_key]["GpuUsage"] = str(util_rate.gpu) + "%"
    except:
        pass

    metrics["Time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return json.dumps(metrics, sort_keys=True)


def write_metric(out_file, interval=None):
    '''
    写资源信息到文件中
    :param out_file:
    :param interval:
    :return:
    '''
    if interval != None and interval > 0:
        with open(out_file, "a+") as fw:
            while True:
                fw.write(str(json.loads(get_system_metrics())) + "\n")
                time.sleep(interval)


def test_thread_read_syste_metrics():
    '''
    测试在子进程中读取并打印资源情况
    :return:
    '''

    def log_metrics():
        metrics = get_system_metrics()
        print(metrics)

    my_timer = Timer(0, 1, log_metrics)
    my_timer.start()
    print("start...")
    my_timer.cancel()


test_thread_read_syste_metrics()
if __name__ == "__main__":
    # metrics = get_system_metrics()
    # print(metrics)
    test_thread_read_syste_metrics()
