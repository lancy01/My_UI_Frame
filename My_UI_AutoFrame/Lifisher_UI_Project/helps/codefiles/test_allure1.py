#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_allure1.py
@time: 2020/3/31 14:14
@DESC:
"""

import pytest, os
import allure


class Test(object):
    @allure.feature('登录功能')
    @allure.story('登录成功')
    @allure.title('用例的标题')  # 用例的标题
    @allure.severity('blocker')
    @allure.issue('https://www.baidu.com/')  # 添加权限对应链接
    @allure.testcase('https://www.baidu.com/')  # 添加用例对应链接
    def test_login(self):
        """
        这里是登录成功测试用例
        :return:
        """
        assert 1 == 1

    @allure.severity('critical')
    def test_01(self):
        assert 1 == 1

    @allure.severity('normal')
    def test_02(self):
        assert 1 == 1

    @allure.severity('minor')
    def test_03(self):
        assert 1 == 1

    @allure.severity('trivial')
    def test_04(self):
        assert 1 == 1


if __name__ == "__main__":
    # 生成测试报告json
    pytest.main(["-s", "-q", '--alluredir', '../report-results', 'test_allure1.py'])
    # 将测试报告转为html格式
    split = 'allure ' + 'generate ' + '../report-results ' + '-o ' + '../allure-report ' + '--clean'
    os.system('cd E:/Auto_Test_Framework/test_case')
    print("hello")
    os.system('E:')
    os.system(split)
    print(split)
