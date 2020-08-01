#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: Save_Screenshot.py
@time: 2020/3/27 17:07
@DESC:
"""
import pytest
from selenium import webdriver

driver = None


class SaveScreenShot:

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):

        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call':
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                screen = _capture_screenshot()
                extra.append(pytest_html.extras.png(screen))
                # only add additional html on failure
                extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            report.extra = extra


    def _capture_screenshot():
        return driver.get_screenshot_as_base64()


    @pytest.fixture(scope='session', autouse=True)
    def browser():
        global driver
        if driver is None:
            driver = webdriver.Firefox()
        return driver

    # def save_screenshot(self, img_doc):

    """
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
     """
        # file_name = OUTPUTS_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        # self.driver.save_screenshot(file_name)
        # with open(file_name, mode='rb') as f:
        #     file = f.read()
        # allure.attach(file, img_doc, allure.attachment_type.PNG)
        # # case_logger.info("页面截图文件保存在：{}".format(file_name))