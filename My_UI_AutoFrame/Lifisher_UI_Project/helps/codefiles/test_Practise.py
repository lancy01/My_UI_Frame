#!/usr/bin/python3
# coding:utf-8

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_Practise.py
@time: 2020/3/24 17:02
@DESC:单纯的练习
"""

import allure
import pytest
import os
import logging
from selenium import webdriver


@allure.title("登陆模块")
@allure.feature("功能描述，这是一个模块的具体描述")
# @pytest.mark.usefixtures("访问主页")
class TestPractise:
    """
    验证测试登陆功能
    """
    @allure.title("第一个方法")
    @allure.story("具体功能点，用户密码正确，可以登陆成功")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize('info',LD.login_normal_data)
    @allure.step("测试登陆成功")
    # @pytest.mark.run(order=1)
    @allure.feature("测试成功的用例")
    @allure.issue(url="http://192.168.1.200:8888/zentao", name="禅道bug跟踪系统")
    @allure.link(url="http://192.168.2.75:8080/BusinessMACenter/", name="测试系统url地址")
    @allure.testcase(url="http://192.168.1.200:8888/zentao", name="测试用例url地址")
    @allure.epic("epic对大Story的一个描述性标签")
    def test_one(self):
        with allure.step("第1步，执行操作1"):
            print("test_one方法执行")
        with allure.step("第2步，执行操作2"):
            assert 1 == 1
        """
        1.feature——测试用例特性（主要功能模块）
        2.story——"feature"功能模块下的分支功能
        3.severity——测试用例的严重级别
        Allure中对严重级别的定义：
            blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
            critical级别：临界缺陷（ 功能点缺失）
            normal级别：普通缺陷（数值计算错误）
            minor级别：次要缺陷（界面错误与UI需求不符）
            trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
　　         使用方法：@allure.severity(allure.severity_level.CRITICAL)  或者  @allure.severity('critical')
        4.step——测试用例的步骤,使用方法：
            1.@allure.step()  只能以装饰器的形式放在类或者方法上面　　
            2.with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
        5.attach——用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
　　      使用方法：allure.attach(body, name, attachment_type, extension)
            body- 要写入文件的原始内容
            name- 包含文件名的字符串
            attachment_type- 其中一个allure.attachment_type值
            extension- 提供的将用作创建文件的扩展名
        6.link/issue/testcase——链接
　　      使用方法：
            @allure.link()
            @allure.issue() 	关联bug系统地址
            1个测试用例可以有多个bug,bug可以只写地址,bug可以只写名称,支持继承，方法继承类上的公共issue
            @allure.testcase()
        7.description——用例描述
　　      使用方法：
            @allure.description()  提供描述字符串的装饰器
            @allure.description_html()  提供一些HTML在测试用例的描述部分
        """
        # with allure.step('1.输入用户名:{} 2.输入密码:{} 3.点击登陆{}'.format(info["username"],info["password"])):
        #     access_home_page[0].login(info["username"],info["password"])

    @allure.title("第二个方法")
    @allure.description("详细描述")
    @allure.step("测试登陆失败")
    @allure.feature("测试失败的用例")
    def test_two(self):
        print("test_two方法执行")
        assert "s" in "loves"

    @allure.title("第三个方法")
    @allure.description("详细描述")
    def test_three(self):
        print("test_three方法执行")
        assert 3 - 2 == 1

    @allure.title("第四个方法")
    @allure.description("详细描述")
    # @pytest.mark.last
    def test_four(self):
        print("test_four方法执行")
        assert 8 - 7 == 1

    @allure.title("第五个方法")
    @allure.description("详细描述")
    def test_five(self):
        print("test_five方法执行")
        assert 11 - 7 == 4

    @allure.title("第六个方法")
    @allure.description("详细描述第六个测试用例")
    def test_six(self):
        print("test_six方法执行")
        assert 11 + 7 == 18
    # driver = webdriver.Chrome()
    # driver.find_element_by_xpath('//*[@id="mainMenu"]/div[2]/a[7]/span')
    # driver.get('http://192.168.2.75:8080/BusinessMACenter/')


if __name__ == "__main__":
    print(__name__)
    pytest.main(["-s", "-q", "test_Practise.py"])
    os.system("allure generate ../../../report-results -o ../../../allure-report --clean")
    # os.system('allure open allure-report')


