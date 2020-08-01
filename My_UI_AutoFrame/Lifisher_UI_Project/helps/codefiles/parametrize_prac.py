#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: parametrize_prac.py
@time: 2020/4/3 10:15
@DESC:
"""

from selenium import webdriver
from time import sleep
import pytest
import allure
import os


list1 = ['1', '5', '9', '2', '10']
str1 = ['a', 'c', 'd', 'e', 'o']


@pytest.mark.parametrize('num,str2', [(list1[0], str1[0]), (list1[1], str1[1]), (list1[2], str1[2])])
def test_aa(num, str2):
    assert num == '1' and str2 == 'a'


parametrize = [(list1, str1)]
@pytest.mark.parametrize('num,str2', parametrize)
def test_bb(num, str2):
    for num1 in num:
        assert num1 == '2'
    for str3 in str2:
        print(str3)
        assert str3 is 'o'



@pytest.mark.parametrize('num', list1)
def test_cc(num):
    assert num == '10'


if __name__ == "__main__":

    pytest.main(['parametrize_prac.py'])
