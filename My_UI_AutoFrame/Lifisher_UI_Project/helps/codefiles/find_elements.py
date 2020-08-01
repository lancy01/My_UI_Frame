"""
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 16:22
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : find_elements.py
# @Software: PyCharm
# @DESC    :重新定义八大定位方法
"""
from selenium import webdriver


class GetEle(object):
    def __init__(self, driver):
        self.driver = driver

    # 定位单个页面元素
    def find_element_by_id(self, *loc):
        return self.driver.find_element_by_id(*loc)

    def find_element_by_name(self, *loc):
        return self.driver.find_element_by_name(*loc)

    def find_element_by_class_name(self, *loc):
        return self.driver.find_element_by_class_name(*loc)

    def find_element_by_xpath(self, *loc):
        return self.driver.find_element_by_xpath(*loc)

    def find_element_by_tag_name(self, *loc):
        return self.driver.find_element_by_tag_name(*loc)

    def find_element_by_link_text(self, *loc):
        return self.driver.find_element_by_link_text(*loc)

    def find_element_by_partial_link_text(self, *loc):
        return self.driver.find_element_by_partial_link_text(*loc)

    def find_element_by_css_selector(self, *loc):
        return self.driver.find_element_by_css_selector(*loc)

    # 定位页面元素，返回多个
    def find_elements_by_id(self, *loc):
        return self.driver.find_elements_by_id(*loc)

    def find_elements_by_name(self, *loc):
        return self.driver.find_elements_by_name(*loc)

    def find_elements_by_class_name(self, *loc):
        return self.driver.find_elements_by_class_name(*loc)

    def find_elements_by_xpath(self, *loc):
        return self.driver.find_elements_by_xpath(*loc)

    def find_elements_by_tag_name(self, *loc):
        return self.driver.find_elements_by_tag_name(*loc)

    def find_elements_by_link_text(self, *loc):
        return self.driver.find_element_by_link_text(*loc)

    def find_elements_by_partial_link_text(self, *loc):
        return self.driver.find_elements_by_partial_link_text(*loc)

    def find_elements_by_css_selector(self, *loc):
        return self.driver.find_elements_by_css_selector(*loc)

    # 定义打开网址
    def open_page(self, url):
        self.driver.get(url)

    # 获取当前页面标题
    def get_title(self):
        return self.driver.current_url

    # 设置窗口最大化
    def maximize_window(self):
        return self.driver.maximize_window()

    # 设置窗口指定大小
    def set_window_size(self,x ,y):
        return self.driver.set_window_size(x, y)

    # 设置隐性等待方法
    def implicitly_wait(self, i):
        return self.driver.implicitly_wait(i)

    # 设置执行js脚本方法,例子如下
    # target = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[2]/a[3]/img')
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    def execute_script(self, s, target):
        return self.driver.execute_script("arguments[0].scrollIntoView();", target)
