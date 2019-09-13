# -*- coding: utf-8 -* -
'''
文件路径相关操作
'''
import glob
import os
import shutil

# 常用相关操作
'''
shutil.copyfile("oldfile","newfile")        # 复制文件
shutil.copy("oldfile","newfile")            # 复制文件夹
os.rename("oldname","newname")              # 重命名文件或文件夹
shutil.move("oldpos","newpos")              # 移动文件夹
os.remove("file")                           # 删除文件
os.rmdir("dir")                             # 删除文件夹，只能是空文件夹
shutil.rmtree("dir")                        # 删除文件夹，有没有内容都可以删除
os.mkdir("dir")                             # 创建文件夹
open("text.txt","w")                        # 创建文件（当文件不存在时）  
'''

test_path = "../../python/"

def read_file_lines(filepath):
    '''
    按行读取文件
    :param filepath:
    :return:
    '''
    with open(filepath,"r") as fr:
        lines = [line.strip("\n") for line in fr]
        # 或者：lines = [line.strip("\n") for line in fr.readlines()]
    return lines

def create_dir(dirpath):
    '''
    如果文件夹不存在，则创建
    :param dirpath:
    :return:
    '''
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def traverse_dir_withsub(dirpath):
    '''
    遍历文件夹下返回所有的文件，包括子目录
    :param dirpath:
    :return:
    '''
    file_list = []
    files = os.listdir(dirpath)
    for fi in files:
        fi_d = os.path.join(dirpath, fi)
        if os.path.isdir(fi_d):
            traverse_dir_withsub(fi_d)
        else:
            file_list += os.path.join(dirpath, fi_d)
    return file_list

def traverse_dir(dirpath):
    '''
    遍历文件夹下所有的文件，不包括子目录
    :param dirpath:
    :return:
    '''
    file_list = []
    for fpathe, dirs, fs in os.walk(dirpath):
        for f in fs:
            file_list += os.path.join(fpathe, f)
    return file_list

def glob_files(dirpath):
    '''
    在指定的文件夹下寻找指定的文件，可以匹配子目录
    :return:
    '''
    file_list = glob.glob(os.path.join(dirpath,"*/*.py"))
    print(file_list)
    return file_list

def get_relative_path(path):
    '''
    绝对路径转相对路径
    :param path:
    :return:
    '''
    realpath = os.path.realpath(path)
    print(realpath)
    return realpath

def get_abs_path(path):
    '''
    相对路径转绝对路径
    :param path:
    :return:
    '''
    abspath = os.path.abspath(path)
    print(abspath)
    return abspath

if __name__ == "__main__":
    # glob_files(test_path)
    print(read_file_lines("test.txt"))