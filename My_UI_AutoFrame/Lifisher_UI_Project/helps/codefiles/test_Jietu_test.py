#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_Jietu_test.py
@time: 2020/3/30 15:37
@DESC:
"""


from selenium import webdriver
from time import sleep
import time
url_login="http://192.168.2.170:8080/WisonManageCenter/"
driver=webdriver.Firefox()
driver.get(url_login)
try:
    driver.find_element_by_id("j_username").send_keys("admin")
    sleep(1)
    driver.find_element_by_id("j_password").send_keys("11")
    # 登录id是错的，定位会抛出异常
    # driver.find_element_by_id("btn_pwd_login").click()
    driver.find_element_by_id("signin1").click()
    driver.quit()
except Exception as msg:
    print(u"异常原因 %s"%msg)
    # 图片名称可以加个时间戳
    nowTime = time.strftime("%Y%m%d-%H-%M-%S")
    t = driver.get_screenshot_as_file("%s.png" % nowTime)
    t1 = driver.get_screenshot_as_file()

    print(u"截图结果: %s"%t)
    driver.quit()
