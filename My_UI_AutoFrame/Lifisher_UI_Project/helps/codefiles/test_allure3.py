#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_allure3.py
@time: 2020/3/31 16:38
@DESC:
"""

# coding:utf-8
from selenium import webdriver
import time
from time import sleep

# 初始设置
# driver = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Users\46322\AppData\Local\Google\Chrome\Application\chromedriver.exe")
driver.get("http://192.168.2.170:8080/WisonManageCenter/")
driver.maximize_window()
time.sleep(1)

# 执行登录操作
driver.find_element_by_id("j_username").clear()
driver.find_element_by_id("j_username").send_keys("admin")
sleep(1)
driver.find_element_by_id("j_password").clear()
driver.find_element_by_id("j_password").send_keys("111")
sleep(1)
driver.find_element_by_id("btn_pwd_login").click()

# 获取登录失败的弹框提示，判断如果有提示，即为登录失败，截图保存；
# res = driver.find_element_by_link_text("登陆失败:")
res = driver.find_element_by_partial_link_text("登陆失败:")
if res:
    driver.get_screenshot_as_file("E:\\Auto_Test_Framework\\screen-shoots\\png\\loginfai3.png")
    print("登录失败...")
else:
    print("登录成功...")