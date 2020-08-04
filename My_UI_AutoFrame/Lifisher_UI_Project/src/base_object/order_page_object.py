from selenium.webdriver.common.by import By
from Lifisher_UI_Project.src.base_common.base_action import BaseAction

# 对象层 继承 基础公共方法
class OrderPageObject(BaseAction):

    # 元素定位：鼠标移动到：营销工具tab
    ele_tool_tab_loc = (By.XPATH, '//*[@id="__layout"]/div/header/div/div[2]/nav/a[4]/span')
    # 元素定位：选择 领英自动找客户 点击
    ele_linkdin_tab_loc = (By.XPATH,'//*[@id="__layout"]/div/header/div/div[2]/nav/a[4]/div/div[2]/div/a[3]')
    # 元素定位：领英版本中的一个立即购买
    ele_buy_linkdin_loc = (By.XPATH, '//*[@id="tool_superiority"]/div[1]/ul/li[1]/div[2]/div[3]')
    # 元素定位：支付宝
    ele_pay_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/dl[1]/div/dd/div/button/span')
