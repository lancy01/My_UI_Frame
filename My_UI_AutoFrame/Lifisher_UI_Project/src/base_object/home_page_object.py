from selenium.webdriver.common.by import By
from Lifisher_UI_Project.src.base_common.base_action import BaseAction

# 对象层 继承 基础公共方法
class HomePageObject(BaseAction):

    # 元素定位：首页
    ele_home_loc = (By.XPATH, '//*[@id="__layout"]/div/header/div/div/div[2]/nav/a[1]/span')

    # 元素定位：海外营销生态服务平台－立即查看
    ele_overseas_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/a')

    # 元素定位：免费试用－立即体验
    ele_free_trial_loc = (By.XPATH,'//*[@id="__layout"]/div/div[1]/ul[1]/li[1]/div[3]/div')
    # 元素定位：活动促销
    ele_event_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[1]/li[2]')
    # 元素定位：活动促销－立即体验
    ele_event_promotion_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[1]/li[2]/div[3]/div')
    # 元素定位：加盟小渔夫
    ele_fisher_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[1]/li[3]')
    # 元素定位：加盟小渔夫－立即体验
    ele_join_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[1]/li[3]/div[3]/div')

    # 元素定位：外贸学院－精选好课－查看详情
    ele_course_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/ul/li[1]/div[2]/a')
    # 元素定位：外贸学院－Google Analyticw工具基础－立即学习
    ele_tool_foundation_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/ul/li[2]/div[2]/a')
    # 元素定位：外贸学院 Facebook广告基础篇
    ele_ad_foundation_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/ul/li[3]/div[2]/a')

    # 元素定位：智能云站-立即试用
    ele_intelligent_cloud_station_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[3]/div/div[1]')
    # 元素定位：云站解决方案－查看详情
    ele_solution_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[3]/div/div[2]/div[1]/a')

    # 元素定位：体验版－立即购买
    ele_experience_edition_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[2]/li[1]/div[2]')
    # 元素定位：标准版－立即购买
    ele_standard_edition_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[2]/li[2]/div[2]')
    # 元素定位：旗舰版-立即购买
    ele_ultimate_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/ul[2]/li[3]/div[2]')

    # 营销工具－社媒询盘猎手
    ele_social_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[1]/li[1]')
    # 营销工具－社媒询盘猎手-立即购买
    ele_social_media_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[2]/li[1]/div/a')
    # 营销工具－领英自动找客户
    ele_lingying_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[1]/li[2]')
    # 营销工具－领英自动找客户－立即购买
    ele_linkdin_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[2]/li[2]/div/a')
    # 营销工具－社媒自动化运营
    ele_shemei_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[1]/li[3]')
    # 营销工具－社媒自动化运营－立即购买
    ele_social_media_automation_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[2]/li[3]/div/a')
    # 营销工具－SEO自动化营销
    ele_seoauto_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[1]/li[4]')
    # 营销工具－SEO自动化营销－立即购买
    ele_seo_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[4]/div/ul[2]/li[4]/div/a')

    # 外贸资讯－查看更多
    ele_foreign_trade_information_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[6]/div/a')

    # 小渔夫－海外营销生态服务平台－立即开启
    ele_open_now_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[7]/a')
