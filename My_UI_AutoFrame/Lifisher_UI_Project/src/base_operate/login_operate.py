from Lifisher_UI_Project.src.base_object.login_page_object import LoginPageObject
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 操作层 继承 对象层
class LoginOperate(LoginPageObject):

    def click_ele_login_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_login_loc).click()
        else:
            target = driver.find_element(*self.ele_login_loc)

    def send_ele_tel_loc(self, driver,tel):
        driver.find_element(*self.ele_tel_loc).send_keys(tel)

    def send_ele_password_loc(self, driver, password):
        driver.find_element(*self.ele_password_loc).send_keys(password)

    def click_ele_log_in_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_log_in_loc).click()
        else:
            target = driver.find_element(*self.ele_log_in_loc)


    def login(self, driver, is_click, tel, password):

        self.click_ele_login_loc(driver , is_click)
        sleep(1)
        self.send_ele_tel_loc(driver, tel)
        sleep(1)
        self.send_ele_password_loc(driver, password)
        sleep(1)
        self.click_ele_log_in_loc(driver, is_click)
        sleep(1)