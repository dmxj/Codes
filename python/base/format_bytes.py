# -*- coding: utf-8 -* -
'''
将字节转换成可读的单位
'''
def bytes(bytes):
    if bytes < 1024:  #比特
        bytes = str(round(bytes, 2)) + ' B' #字节
    elif bytes >= 1024 and bytes < 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024, 2)) + ' KB' #千字节
    elif bytes >= 1024 * 1024 and bytes < 1024 * 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024 / 1024, 2)) + ' MB' #兆字节
    elif bytes >= 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024 / 1024 / 1024, 2)) + ' GB' #千兆字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024 / 1024 / 1024 / 1024, 2)) + ' TB' #太字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' PB' #拍字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes * 1.0 / 1024 / 1024 / 1024 / 1024 / 1024 /1024, 2)) + ' EB' #艾字节
    return bytes

if __name__ == "__main__":
    print(bytes(54088302592))