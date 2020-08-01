"""
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:49
# @Author  : swyang
# @contact    : 463222072@qq.com
# @File    : test_log_new0629.py
# @Software: PyCharm
# @DESC    :
"""
import pytest
import logging
from logging.config import fileConfig
from os import path


class TestLogs(object):
    @pytest.mark.usefixtures("log_record")
    def test_log1(self, log_record):
        log_record.warning("这个是告警信息")


if __name__ == '__main__':
    print(__name__)
    pytest.main(["-s", "-q", "test_log_new0629.py"])
    # os.system("allure generate ../../../report-results -o ../../../allure-report --clean")


