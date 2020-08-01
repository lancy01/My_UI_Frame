"""
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 14:19
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : test_c.py
# @Software: PyCharm
# @DESC    :
"""
from selenium import webdriver
from time import sleep
import pytest
import allure
import os
from selenium.webdriver.common.by import By

driver = None


def test_c():
    driver1 = webdriver.Chrome("../../../drivers/chromedriver.exe")
    driver1.get("http://study.bweyes.cn")
    driver1.get_screenshot_as_file("F:\\haha.png")



test_c()

