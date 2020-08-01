"""
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 16:04
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
# @DESC    :
"""

from selenium import webdriver
from time import sleep
import pytest
import allure
import os
from selenium.webdriver.common.by import By

driver = None
