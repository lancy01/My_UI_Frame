#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: test_html_seletor.py
@time: 2020/4/7 16:00
@DESC:
"""

from selenium import webdriver
from time import sleep
import pytest
import allure
import os


def test_seletor1():
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.75:8080/BusinessMACenter/")

    # driver.find_element_by_id()
    # driver.find_elements_by_name()
    # driver.find_element_by_class_name()
    # driver.find_element_by_link_text()
    # driver.find_element_by_partial_link_text()
    # driver.find_elements_by_css_selector()
    # driver.find_element_by_xpath()
    # driver.find_elements_by_tag_name()


if __name__ == "__main__":

    test_seletor1()

