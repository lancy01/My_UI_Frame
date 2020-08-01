from Lifisher_UI_Project.src.base_object.order_page_object import OrderPageObject

# 操作层 继承 对象层
class OrderOperate(OrderPageObject):

    # 通过继承覆盖方法：如果子类和父类的方法名称相同，优先使用子类自己的方法
    def open(self, driver, page_title):
        self._open(driver, page_title)

    # 操作：点击 领英自动找客户tab 页 *self.ele_linder_tab_loc 理解为对象self 调用变量
    def click_ele_linder_tab_loc(self, driver):
        driver.find_element(*self.ele_linder_tab_loc).click()

    # 操作：点击 立即购买按钮
    def click_ele_buy_linder_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_buy_linder_loc).click()
        else:
            target = driver.find_element(*self.ele_buy_linder_loc)
            return target

    # 返回指定的元素值(支付方式)
    def get_pay_text(self,driver):
        return driver.find_element(*self.ele_pay_loc).text



