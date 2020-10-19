from Lifisher_UI_Project.src.base_object.home_page_object import HomePageObject
from selenium.webdriver.common.action_chains import ActionChains

# 操作层 继承 对象层
class HomeOperate(HomePageObject):

    # 通过继承覆盖方法：如果子类和父类的方法名称相同，优先使用子类自己的方法
    def open(self, driver, page_title):
        self._open(driver, page_title)

    # 点击：首页 菜单
    def click_ele_home_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_home_loc).click()
        else:
            target = driver.find_element(*self.ele_home_loc)
            return target

    # 点击：海外营销生态服务平台－立即查看
    def click_ele_overseas_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_overseas_loc).click()
        else:
            target = driver.find_element(*self.ele_overseas_loc)
            return target

    # 点击：免费试用－立即体验
    def click_ele_free_trial_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_free_trial_loc).click()
        else:
            target = driver.find_element(*self.ele_free_trial_loc)
            return target

    # 移动：鼠标移动到 活动促销
    def move_ele_event_loc(self, driver):
        ele = driver.find_element(*self.ele_event_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：活动促销－立即体验
    def click_ele_event_promotion_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_event_promotion_loc).click()
        else:
            target = driver.find_element(*self.ele_event_promotion_loc)
            return target

    # 移动：鼠标移动到 加盟小渔夫
    def move_ele_fisher_loc(self, driver):
        ele = driver.find_element(*self.ele_fisher_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：加盟小渔夫－立即体验
    def click_ele_join_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_join_loc).click()
        else:
            target = driver.find_element(*self.ele_join_loc)
            return target

    # 点击：外贸学院－精选好课－查看详情
    def click_ele_course_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_course_loc).click()
        else:
            target = driver.find_element(*self.ele_course_loc)
            return target

    # 点击：外贸学院－Google Analyticw工具基础－立即学习
    def click_ele_tool_foundation_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_tool_foundation_loc).click()
        else:
            target = driver.find_element(*self.ele_tool_foundation_loc)
            return target

    # 点击：外贸学院－Facebook广告基础篇－立即学习
    def click_ele_ad_foundation_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_ad_foundation_loc).click()
        else:
            target = driver.find_element(*self.ele_ad_foundation_loc)
            return target

    # 点击：智能云站－立即试用
    def click_ele_intelligent_cloud_station_loc(self, driver,is_click):
        if is_click is True:
            driver.find_element(*self.ele_intelligent_cloud_station_loc).click()
        else:
            target = driver.find_element(*self.ele_intelligent_cloud_station_loc)
            return target

    # 点击：云站解决方案－查看详情
    def click_ele_solution_loc(self, driver,is_click):
        if is_click is True:
            driver.find_element(*self.ele_solution_loc).click()
        else:
            target = driver.find_element(*self.ele_solution_loc)
            return target

    # 点击：标准版－立即购买
    def click_ele_experience_edition_loc(self, driver,is_click):
        if is_click is True:
            driver.find_element(*self.ele_experience_edition_loc).click()
        else:
            target = driver.find_element(*self.ele_experience_edition_loc)
            return target

    # 点击：标准版－立即购买
    def click_ele_standard_edition_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_standard_edition_loc).click()
        else:
            target = driver.find_element(*self.ele_standard_edition_loc)
            return target

    # 点击：旗舰版－立即购买
    def click_ele_ultimate_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_ultimate_loc).click()
        else:
            target = driver.find_element(*self.ele_ultimate_loc)
            return target

    # 移动：鼠标移动到 社媒询盘猎手
    def move_ele_social_loc(self, driver):
        ele = driver.find_element(*self.ele_social_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：社媒询盘猎手－立即购买
    def click_ele_social_media_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_social_media_loc).click()
        else:
            target = driver.find_element(*self.ele_social_media_loc)
            return target

    # 移动：鼠标移动到 领英自动找客户
    def move_ele_lingying_loc(self, driver):
        ele = driver.find_element(*self.ele_lingying_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：领英自动找客户－立即购买
    def click_ele_linkdin_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_linkdin_loc).click()
        else:
            target = driver.find_element(*self.ele_linkdin_loc)
            return target

    # 移动：鼠标移动到 社媒自动化运营
    def move_ele_shemei_loc(self, driver):
        ele = driver.find_element(*self.ele_shemei_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：社媒自动化运营－立即购买
    def click_ele_social_media_automation_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_social_media_automation_loc).click()
        else:
            target = driver.find_element(*self.ele_social_media_automation_loc)
            return target

    # 移动：鼠标移动到SEO 自动化运营
    def move_ele_seoauto_loc(self, driver):
        ele = driver.find_element(*self.ele_seoauto_loc)
        ActionChains(driver).move_to_element(ele).perform()

    # 点击：SEO 自动化运营－立即购买
    def click_ele_seo_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_seo_loc).click()
        else:
            target = driver.find_element(*self.ele_seo_loc)
            return target

    # 点击：外贸资讯－查看更多
    def click_ele_foreign_trade_information_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_foreign_trade_information_loc).click()
        else:
            target = driver.find_element(*self.ele_foreign_trade_information_loc)
            return target

    # 点击：小渔夫－海外营销生态服务平台－立即开启
    def click_ele_open_now_loc(self, driver, is_click):
        if is_click is True:
            driver.find_element(*self.ele_open_now_loc).click()
        else:
            target = driver.find_element(*self.ele_open_now_loc)
            return target


