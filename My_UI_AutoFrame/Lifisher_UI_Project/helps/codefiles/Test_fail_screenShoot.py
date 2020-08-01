#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: Test_fail_screenShoot.py
@time: 2020/3/30 15:20
@DESC:
"""

import pytest
import allure
from time import sleep
import os.path
from selenium import webdriver

from os import path
from selenium.common.exceptions import NoSuchElementException

"""
try:
    except Exception:
    print("Error：啊哦，出异常了")

else:
print("用例执行ok")
finally:
"""


class TestFailScreenShoot(object):

    def test_run001(self):
        assert 1 == 2

    def test_run002(self):
        assert 1 == 1

    def test_screenshot_on_test_failure(self, browser, log_record):
        browser.get("http://192.168.2.75:8080/BusinessMACenter/")
        sleep(1)
        log_record.info("输入用户名")
        browser.find_element_by_id("j_username").send_keys("admin")
        sleep(1)
        log_record.info("输入密码")
        browser.find_element_by_id("j_password").send_keys("111")
        browser.fullscreen_window()
        sleep(1)
        browser.set_window_size(1920, 1080)
        # 登录id是错的，定位会抛出异常
        # driver.find_element_by_id("btn_pwd_login").click()
        browser.find_element_by_id("signin1").click()
        browser.quit()


if __name__ == "__main__":

     pytest.main(['-v', '-s', 'Test_fail_screenShoot.py'])
     os.system("allure generate ../report-results -o ../allure-report --clean")
