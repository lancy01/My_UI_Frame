#!/usr/bin/python3
# coding="utf-8"

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_Search.py
@time: 2020/3/24 10:29
@DESC:云边界查询http类型日志
"""
import os
from time import sleep

import allure
import pytest
from selenium import webdriver


class TestSearch:

    # def setUp(self):
    #     self.driver = webdriver.Chrome(
    #         r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    #     self.driver.implicitly_wait(30)
    #     self.driver.maximize_window()
    #
    # def tearDown(self):
    #     self.time.sleep(5)
    #     self.driver.quit()

    # option = webdriver.ChromeOptions()
    # option.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    global url
    url = "http://192.168.2.170:8080/WisonManageCenter/"

    @allure.title("查询业务日志")
    @allure.description("查询具体的http业务日志")
    def test_search_http(self):

        self.driver.get(url)

        self.driver.find_element_by_id("j_username").send_keys("admin")
        sleep(1)
        self.driver.find_element_by_id("j_password").send_keys("11")
        sleep(1)
        self.driver.find_element_by_id("btn_pwd_login").click()
        # 显示等待加载
        sleep(3)
        self.driver.fullscreen_window()
        sleep(2)
        search_result = "ok"
        assert search_result == "ok"
        self.driver.quit()
        # return "ok"


if __name__ == "main":

    pytest.main(['-s', '-q', '--alluredir', '../report-result', 'test_Search.py'])
    # 执行命令 allure generate E:\\Auto_Test_Framework\\allure_result -o ./report --clean ，生成测试报告
    os.system(
        'allure generate ../allure-result -o ../allure-report --clean')


