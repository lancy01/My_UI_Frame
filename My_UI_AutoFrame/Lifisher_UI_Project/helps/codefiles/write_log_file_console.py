"""
# -*- coding: utf-8 -*-
@Time    : 2020/7/6 15:38
@Author  : swyang
@contact    : 463222072@qq.com
@File    : write_log_file_console.py
@Software: PyCharm
@DESC    :
"""
import sys


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger("../../allure-logs//a.log", sys.stdout)
sys.stderr = Logger("../../allure-logs/a.log_file", sys.stderr)  # redirect std err, if necessary

# now it works
print("something")
# logger = Logger()
# logger.write("娃哈哈矿泉水")


