#!/usr/bin/python
# coding:utf-8

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: pytest_practice01.py
@time: 2020/1/7 14:38
@DESC:
"""
import pytest
import allure
import allure_pytest
from time import sleep
from selenium import webdriver
import xdist
import xlrd


def test1_01(a, b):

    return a+b
"""
鼠标事件
context_click 右击事件
double_click 双击事件
drag_and_drop 拖动
move_to_element() 鼠标停在一个元素上
click_and_hold 按下鼠标左键在一个元素上

键盘事件
from selenium.webdriver.common.keys import Keys
send_kyes(Kyes.BACK_SPACE) 退格键
send_kyes(Kyes.CONTRL, 'a') 全选
send_kyes(Kyes.CONTRL, 'v') 粘贴
send_kyes(Kyes.CONTRL, 'c') 复制
send_kyes(Kyes.CONTRL, 'x') 剪切
send_kyes(Kyes.ENTER)       回车
"""

"""
标签 
　　这个标签非常好用
　　@allure.feature 　　分组第一层
　　@allure.story　　分组第二层
　　@allure.severity    标记严重级别
"""
# @allure.title("woqu")
# @allure.description("这是一个测试描述")
# @allure.testcase("http://192.168.60.30:8080/BusinessMACenter/index/main.do","集约化平台")
# @allure.attach("报告显示内容","要显示的附件名称","附件的类型")

# @pytest.fixture(scope="session")
# @allure.step('这里是操作步骤的描述： 获取参数一：“{0}”，获取参数二： “{1}” ')
# @pytest.mark.parametrize('param1, param2', [(1, 10), (2, 20)])
# @allure.severity(allure.severity_level.BLOCKER)
# @allure.testcase()
# @allure.link('http://baidu.com', name="link_url")
# @allure.issue('http://baidu.com', name='点击我跳转百度')
# @allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
def test_assert():

    a = 6
    b = 3
    assert test1_01(a, b) == 8


if __name__ == "__main__":

    pytest.main(["-s", "-q", "pytest_practice01.py"])

