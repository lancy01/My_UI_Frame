#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: exception_log.py
@time: 2020/3/30 11:53
@DESC:
"""

import logging
import traceback
from os import path
from logging.config import fileConfig

# logging.basicConfig(filename='log.txt', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
log_file_path = path.join(path.dirname(path.abspath(__file__)), '../conf/logconf.ini')

# 读取日志配置文件内容
logging.config.fileConfig(log_file_path)

# 创建一个日志器logger
logger = logging.getLogger('fmt')

try:
    raise Exception('发生异常错误信息')
except:
    # 方案一，自己定义一个文件，自己把错误堆栈信息写入文件。
    # errorFile = open('log.txt', 'a')
    # errorFile.write(traceback.format_exc())
    # errorFile.close()

    # 方案二，使用Python标准日志管理维护工具。
    # logging.debug(traceback.format_exc())
    logger.debug(traceback.format_exc())

