#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pytest
import allure
import os
from selenium.webdriver.common.by import By
driver = None


class TestLogin:

    # driver = webdriver.Firefox()
    # driver = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    # driver = webdriver.Chrome(r"C:\Users\46322\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    # global url
    # url = "http://192.168.2.170:8080/WisonManageCenter/"

    def login_by(self):
        """
        比较底层，只作为了解即可
        find_element_by_id官方建议使用这种方式。
        :return:
        """
        # self.driver.get(url)
        driver = webdriver.Chrome()
        driver.find_element(By.ID,"j_username").send_keys("admin")
        driver.find_element(By.ID, "j_password").send_keys("11")
        driver.find_element(By.CLASS_NAME, "")
        driver.find_element(By.NAME, "")
        driver.find_element(By.TAG_NAME, "")
        driver.find_element(By.LINK_TEXT, "")
        driver.find_element(By.PARTIAL_LINK_TEXT, "")
        driver.find_element(By.CSS_SELECTOR, "")
        driver.find_element(By.XPATH, "")
        driver.find_element_by_xpath("")

    @allure.description("这里可以写详细说明")
    @allure.title("这是个标题")
    @pytest.mark.run(order=1)
    # @pytest.mark.usefixtures("browser1")
    def test_login(self, browser):
        """
        Pytest 测试样例规范
        1.测试文件以 test_ 开头（以 _test 结尾也可以）
        2.测试类以 Test 开头，并且不能带有 __init__ 方法
        3.测试函数以 test_ 开头
        4.断言使用基本的 assert 即可
        :return:
        """
        browser.get("http://study.bweyes.cn")
        # driver.get(url)
        # browser.find_element_by_id("j_username").send_keys("admin")
        # sleep(1)
        # browser.find_element_by_id("j_password").send_keys("11")
        # browser.find_element_by_id("j_password").send_keys("wison@2015")
        # sleep(1)
        # browser.find_element_by_id("btn_pwd_login").click()
        # sleep(3)
        # browser.fullscreen_window()
        # browser.find_element_by_class_name("dropdown-toggle").click()
        # browser.find_element_by_link_text("退出登录").click()

        # self.driver.find_element_by_link_text("确定").click()
        # browser.find_element_by_class_name("layui-layer-btn0").click()
        # self.driver.find_element_by_link_text("确定")
        # browser.find_elements_by_css_selector(self, "#layui-layer1>div.layui-layer-btn>a.layui-layer-btn0").click()
        # alert1 = browser.switch_to.alert()
        # alert1.accept()
        # self.driver.find_elements_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')
        print(browser.get_window_size())
        sleep(1)
        browser.set_window_size(1920, 1280)
        # self.driver.fullscreen_window()
        # self.driver.refresh()
        # sleep(2)
        # browser.fullscreen_window()
        # 显示等待加载
        sleep(2)
        # browser.close()
        # browser.quit()

        assert "ok" == 'ok'

    # pytest的使用函数
    # @allure.title("登录集约化平台")
    # @allure.description("这里可以写详细说明")
    # @pytest.mark.run(order=1)
    # def test_login(self, browser):
    #     driver1 = browser.get("http://192.168.2.75:8080/BusinessMACenter/")
    #     # print("pytest进来了")
    #     # with open('..\images\wison-test.png',mode='rb') as f:
    #     #     file = f.read()
    #     # with allure.step('添加失败截图...'):
    #     #     allure.attach(driver, '图片描述-失败截图', allure.attachment_type.PNG)
    #     login_result = self.login(driver1)
    #     assert login_result == "ok"


if __name__ == "__main__":

    # login1 = TestLogin()
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 E:\\Auto_Test_Framework\\allure_result 目录
    pytest.main(["-s", "-q", "test_Login.py"])
    # os.system("allure generate ../../../report-results -o ../../../allure-report --clean")




