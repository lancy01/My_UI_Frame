#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_allure5.py
@time: 2020/3/31 17:40
@DESC:
"""

# 截图方式二
# coding=utf-8
from selenium import webdriver
import os
import time
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

driver = webdriver.Chrome()
driver.get("https://baidu.com/")
try:
    url=driver.save_screenshot('..\\screen-shoots\\' + directory_time + '\\' + picture_time + '.png')
    print("%s ：截图成功！！！" % url)
except BaseException as pic_msg:
    print("截图失败：%s" % pic_msg)
time.sleep(2)
driver.quit()