#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_Fail1.py
@time: 2020/4/1 18:08
@DESC:
"""

from selenium import webdriver
from time import sleep
import pytest
import allure
import time
import os


def picture_dir():
    # 生成年月日时分秒时间
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    print(picture_time)
    print(directory_time)
    # 打印文件目录
    print(os.getcwd())
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        # os.getcwd(),获取当前工作目录
        File_Path = '..\\screen-shoots\\' + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            print("目录新建成功：%s" % File_Path)
        else:
            print("目录已存在！！！")
    except BaseException as msg:
        print("新建目录失败：%s" % msg)

    url = directory_time + '\\' + picture_time + '.png'
    print(url)
    return url


url = picture_dir()
print(url)



