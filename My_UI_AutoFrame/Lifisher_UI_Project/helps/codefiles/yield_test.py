"""
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 17:54
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : yield_test.py
# @Software: PyCharm
# @DESC    :验证带有yield的函数是否迭代器
"""
from inspect import isgeneratorfunction
import pytest


def test_yield():
    # print(isgeneratorfunction(pytest_runtest_makereport))
    assert 1+2 == 3


if __name__ == '__main__':
    print(__name__)
    pytest.main(["-s", "-q", "yield_test.py"])
