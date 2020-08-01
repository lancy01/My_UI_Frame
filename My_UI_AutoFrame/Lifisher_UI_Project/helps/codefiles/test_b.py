"""
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 11:05
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : test_b.py
# @Software: PyCharm
# @DESC    :
"""

from selenium import webdriver
from time import sleep
import pytest
import allure
import os
from selenium.webdriver.common.by import By
# from ...base_pre_operation import open_browser as br
# 使用相对目录导入包存在bug，不建议使用
from lifisher_pc_project.src.base_pre_operation.find_elements import GetEle
from lifisher_pc_project.src.base_pre_operation.scroll_page import scroll_page


class Test:

    @pytest.mark.usefixtures("login")
    def test_order(self, login):
        driver = GetEle(login)
        # driver.open_page("http://study.bweyes.cn")
        # driver.maximize_window()
        # driver.implicitly_wait(2)
        # 点击工具
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/nav/div[3]/a/span').click()
        sleep(2)
        # 点击 "领英图片链接"
        target = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[2]/a[3]/img')
        driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[2]/a[3]/img').click()
        sleep(2)
        # 页面下拉
        # scroll_page(driver, 3)
        # 点击购买
        page = driver.find_element_by_xpath('//*[@id="tool_edition"]/div/ul/li[2]/div[2]/div[4]/div[2]').click()
        driver.implicitly_wait(10)
        sleep(5)
        assert "支付方式" in page
        # driver.get("http://study.bweyes.cn")


if __name__ == "__main__":
    pytest.main(["test_b.py"])
    # os.system("allure generate ../../../report-results -o ../../../allure-report --clean")
