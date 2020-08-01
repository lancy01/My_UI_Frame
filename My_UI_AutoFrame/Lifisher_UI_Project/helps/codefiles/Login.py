from selenium import webdriver
from time import sleep
import pytest


class Login:
    ## 驱动文件路径
    driverfile_path = r'G:\gittest\wisonautotest4ui\drivers\chromedriver.exe'
    ## 启动浏览器
    driver = webdriver.Chrome(executable_path=driverfile_path)

    def more_elements(self):
        url = "http://192.168.2.170:8080/WisonManageCenter/"
        self.driver.get(url)
        self.driver.set_window_size(1380, 800)
        self.driver.find_elements_by_id("j_username")[0].send_keys("wsa")
        self.driver.find_elements_by_id("j_password")[0].send_keys("wison!@#123")
        self.driver.find_elements_by_id("btn_pwd_login")[0].click()
        self.driver.find_element_by_class_name("dropdown-toggle").click()
        self.driver.find_elements_by_link_text("退出登录")[0].click()
        self.driver.find_elements_by_link_text("确定")[0].click()

        ab = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/div/dl/div/dd/div'
                                               '/button/span').text
        print(ab)
        sleep(3)
        self.driver.quit()
    def single_element(self):

        url = "http://192.168.2.170:8080/WisonManageCenter/"
        self.driver.get(url)
        sleep(2)
        self.driver.set_window_size(1280, 800)
        self.driver.find_element_by_id("j_username").send_keys("wsa")
        self.driver.find_element_by_id("j_password").send_keys("wison!@#123")
        self.driver.find_element_by_id("btn_pwd_login").click()
        sleep(2)
        # self.driver.find_element_by_css_selector(".fa-caret-down").click()
        self.driver.find_element_by_class_name("dropdown-toggle").click()
        # 获取窗口尺寸
        size1=self.driver.get_window_size()
        print(size1)
        sleep(3)
        # 设置窗口尺寸为800*600
        self.driver.set_window_size(800, 600)
        size2=self.driver.get_window_size()
        print(size2)
        self.driver.minimize_window()  # 窗口最小化，窗口尺寸未发生变化
        size3=self.driver.get_window_size()
        print(size3)
        self.driver.maximize_window()  # 窗口最大化
        size4=self.driver.get_window_size()
        print(size4)
        sleep(5)
        self.driver.find_element_by_link_text("退出登录").click()
        self.driver.find_element_by_class_name("layui-layer-btn0").click()
        self.driver.quit()


# 根据 __name__ 判断是否执行下方代码
'''
1. 如果模块是被导入，__name__的值为模块名字
2. 如果模块是被直接执行，__name__的值为’__main__’
'''
if __name__ == "__main__":
    print(__name__)
    login1=Login()
    login1.single_element()




