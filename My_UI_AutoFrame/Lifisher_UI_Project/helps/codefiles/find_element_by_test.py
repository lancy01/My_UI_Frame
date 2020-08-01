"""
# -*- coding: utf-8 -*-
@Time    : 2020/7/6 11:00
@Author  : swyang
@contact    : 463222072@qq.com
@File    : find_element_by_test.py
@Software: PyCharm
@DESC    :
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# # by_id = "id"
# by_xpath = "xpath"
# by_link_text = "link text"
# by_partial_text = "partial link text"
# by_name = "name"
# by_tag_name = "tag name"
# by_class_name = "class name"
# by_css_selector = "css selector"

driver = webdriver.Chrome("../../drivers/chromedriver.exe")
driver.get("https://www.baidu.com/")

driver.find_element("id", "kw").send_keys("selenium")

driver.find_element('css selector', "#su").click()

