from selenium.webdriver.common.by import By
from Lifisher_UI_Project.src.base_common.base_action import BaseAction

# 对象层 继承 基础公共方法
class OrderPageObject(BaseAction):

    # 元素定位：领英拳头单页tab元素
    ele_linder_tab_loc = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[1]/a[1]')
    # 元素定位：领英版本中的一个立即购买
    ele_buy_linder_loc = (By.XPATH, '//*[@id="tool_edition"]/div/ul/li[2]/div[2]/div[4]/div[2]')

    ele_pay_loc = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div/dl[1]/div/dd/div/button/span')
