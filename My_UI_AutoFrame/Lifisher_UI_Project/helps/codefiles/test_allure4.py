#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_allure4.py
@time: 2020/3/31 17:33
@DESC:
"""

# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
print(picture_time)
try:
    picture_url=driver.get_screenshot_as_file('..\\screen-shoots\\png\\'+ picture_time +'.png')
    print("%s：截图成功！！！" % picture_url)
except BaseException as msg:
    print(msg)
driver.quit()