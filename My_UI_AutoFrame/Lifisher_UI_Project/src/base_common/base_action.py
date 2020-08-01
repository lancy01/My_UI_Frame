from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseAction(object):

    driver = None
    js_script_true = "arguments[0].scrollIntoView(true)"
    js_script_false = "arguments[0].scrollIntoView(false)"

    def on_page(self,driver,page_title):
        return page_title in driver.title

    # 以单下划线_开头的方法，在使用inport * 时，该方法不会被导入，保证该方法为类私有的
    def _open(self,driver,page_title):
        assert self.on_page(driver,page_title),  u'打开页面失败'

    def open(self,driver,page_title):
        self._open(driver,page_title)


    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script 方法，用于执行js脚本，定位元素查看位置
    def script_top(self, target, driver):
        driver.execute_script(self.js_script_true, target)

     # 定义script方法，用于执行js脚本，定位元素查看位置
    def script_dowm(self, target, driver):
        driver.execute_script(self.js_script_false, target)


    # 重写元素定位方法
    def find_element(self, *loc):
        try:
            # 确保元素是可见的
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)

        except ValueError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # # 重写元素操作点击click方法
    # def action_click(self, loc):
    #     self.find_element(*loc).click()

    # 重写元素send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc) #getattr 相当于实现 self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" %(self, loc))

    # # 通过键盘操作全选
    # def action_clear(self,loc):
    #     self.find_element(*loc).send_keys(Keys.CONTROL, "a")


















