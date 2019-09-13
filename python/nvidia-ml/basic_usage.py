# -*- coding: utf-8 -* -
'''
nvidia-ml-py是一个用来读取GPU使用显存的数据
对于python3: pip install nvidia-ml-py3
对于python2，也是：pip install nvidia-ml-py3
'''
import pynvml
pynvml.nvmlInit()

# 获取显卡驱动版本号：
driverVersion = pynvml.nvmlSystemGetDriverVersion()
print("显卡驱动版本号：",driverVersion)

# 获取显卡个数：
deviceCount = pynvml.nvmlDeviceGetCount()
print("显卡个数：",deviceCount)

# 获取某个显卡的名称：
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
print("显卡0的名称：",pynvml.nvmlDeviceGetName(handle))

# 获取某个显卡的显存占用信息：
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
print("已使用显存：",meminfo.used)
print("未使用显存：",meminfo.free)
print("总显存大小：",meminfo.total)

# 获取GPU利用率或显存利用率
util_rate = pynvml.nvmlDeviceGetUtilizationRates(handle)
print("显卡GPU利用率：",util_rate.gpu)
print("显卡显存利用率：",util_rate.memory)

