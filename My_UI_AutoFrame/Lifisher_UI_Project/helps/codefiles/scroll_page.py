"""
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 10:12
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : scroll_page.py
# @Software: PyCharm
# @DESC    : 页面下拉功能
"""
from time import sleep


# driver = None
# times = None
def scroll_page(driver, times, target):
    for i in range(times):
        # 下拉三次，这里用到了JavaScript 代码
        driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
