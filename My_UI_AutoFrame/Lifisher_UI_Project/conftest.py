import os
import pytest
import logging
from logging.config import fileConfig


@pytest.fixture(scope='session', autouse=False)
def log_record():
    # 路径计算：相对于执行的模块文件src/test_suite
    log_file_path = os.path.abspath( '../../../conf/logconf.ini')

    # 读取日志配置文件内容
    logging.config.fileConfig(log_file_path)

    # 创建一个日志器logger
    logger = logging.getLogger('fmt')
    return logger



