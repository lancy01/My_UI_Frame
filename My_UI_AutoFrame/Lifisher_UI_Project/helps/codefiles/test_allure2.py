#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_allure2.py
@time: 2020/3/31 15:45
@DESC:
"""

# coding=utf-8
import time

import pytest
import os
import allure
from allure_commons import logger


class TestFailScreenShoot(object):

    def test_run001(self):
        assert 1 == 2

    def test_run002(self):
        assert 1 == 1

    def test_screenshot_on_test_failure(self, browser):
        browser.get("https://www.baidu.com")
        assert False


if __name__ == "__main__":
    # 生成测试报告json
    pytest.main(["-s", "-q", '--alluredir', '../report-results', 'test_allure2.py'])
    # 将测试报告转为html格式
    split = 'allure ' + 'generate ' + '../report-results ' + '-o ' + '../allure-report ' + '--clean'
    os.system('cd E:/Auto_Test_Framework/test_case')
    print("hello")
    os.system('E:')
    os.system(split)
    print(split)
