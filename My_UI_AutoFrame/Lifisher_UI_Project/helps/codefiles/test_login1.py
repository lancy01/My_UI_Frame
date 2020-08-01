#!/usr/bin/python3

from selenium import webdriver
from time import sleep
import pytest
import allure
import os
from selenium.webdriver.common.by import By


class TestLogin1:

    # driver = webdriver.Firefox()
    # driver = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    # driver = webdriver.Chrome(r"C:\Users\46322\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    # global url
    # url = "http://192.168.2.170:8080/WisonManageCenter/"

    def test_login1(self):
        """
        Pytest 测试样例规范
        1.测试文件以 test_ 开头（以 _test 结尾也可以）
        2.测试类以 Test 开头，并且不能带有 __init__ 方法
        3.测试函数以 test_ 开头
        4.断言使用基本的 assert 即可
        :return:
        """
        driver = webdriver.Chrome(r"C:\Users\46322\AppData\Local\Google\Chrome\Application\chromedriver.exe")
        driver.get("http://192.168.2.75:8080/BusinessMACenter/")
        # driver.get(url)
        driver.find_element_by_id("j_username").send_keys("admin")
        sleep(1)
        # browser.find_element_by_id("j_password").send_keys("11")
        driver.find_element_by_id("j_password").send_keys("wison@2015")
        sleep(1)
        driver.find_element_by_id("btn_pwd_login").click()
        driver.set_window_size(1920, 1280)
        sleep(1)
        # browser.fullscreen_window()
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("退出登录").click()
        # browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click
        # alert1 = driver.switch_to.alert
        # alert1 = driver.switch_to.active_element
        driver.find_element_by_class_name("layui-layer-btn0").click()

        # 打印警告对话框内容
        # print(alert1.text)
        print("进来了")
        # alert1.accept()
        # alert1.click()
        # browser.get_window_size()
        # sleep(1)
        # browser.set_window_size(1920, 1280)
        # self.driver.fullscreen_window()
        # self.driver.refresh()
        # sleep(2)
        # browser.fullscreen_window()
        # 显示等待加载
        sleep(2)
        driver.quit()
        # assert "ok" == 'ok'


if __name__ == "__main__":

    login1 = TestLogin1()
    login1.test_login1()
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 E:\\Auto_Test_Framework\\allure_result 目录
    # pytest.main(["-s", "-v", "test_login1.py"])


