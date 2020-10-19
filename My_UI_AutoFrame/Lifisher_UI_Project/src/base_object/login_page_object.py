from selenium.webdriver.common.by import By
from Lifisher_UI_Project.src.base_common.base_action import BaseAction

# 对象层 继承 基础公共方法
class LoginPageObject(BaseAction):

    # 元素定位：登录
    ele_login_loc = (By.XPATH, '//*[@id="__layout"]/div/header/div/div/div[3]/div/a[1]')

    # 元素定位：手机号输入框
    ele_tel_loc = (By.XPATH, '//*[@id="pane-second"]/form/div[1]/div/div[1]/input')

    # 元素定位：密码输入框
    ele_password_loc = (By.XPATH, '//*[@id="pane-second"]/form/div[2]/div/div/input')

    # 元素定位：登录按钮
    ele_log_in_loc = (By.XPATH, '//*[@id="pane-second"]/div[1]')
