#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: logs_new_pro.py
@time: 2020/3/28 17:50
@DESC:
"""
import logging
from logging.config import fileConfig
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), '../conf/logconf.ini')

# 读取日志配置文件内容
logging.config.fileConfig(log_file_path)

# 创建一个日志器logger
logger = logging.getLogger('fmt')
logger.warning("这个是告警信息")


if __name__ == '__main__':

    # 日志输出
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
