from time import sleep
import pytest
import allure
from selenium import webdriver
from Lifisher_UI_Project.src.base_operate.login_operate import LoginOperate
from Lifisher_UI_Project.src.base_operate.home_operate import HomeOperate
from Lifisher_UI_Project.src.test_suite.conftest import *
from Lifisher_UI_Project.src.base_operate.order_operate import OrderOperate

ho = HomeOperate()
oo = OrderOperate()

# 业务层 继承 操作层
@allure.epic("小渔夫生产环境－首页－所有链接检测")
class TestCaseHome(HomeOperate):

    @allure.title("测试用例标题：点击－海外营销生态服务平台－立即查看－页面跳转是否正确")
    @pytest.mark.run(order=1)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_haiwai(self, login):
        driver = login

        page_title = "小渔夫 - 外贸营销综合平台 - 企业出海，找小渔夫"
        with allure.step("1. 验证首页打开是否正确"):
            ho.open(driver, page_title)

        # 点击：海外营销生态服务平台－立即查看
        with allure.step("2. 点击：海外营销生态服务平台－立即查看－检查链接跳转是否正确"):
            ho.click_ele_overseas_loc(driver, True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/toolHome'

        with allure.step("3. 返回首页"):
            ho.click_ele_home_loc(driver, True)
            sleep(3)


    @allure.title("测试用例标题：点击－免费试用/活动促销/加盟小渔夫－立即体验－页面跳转是否正确")
    @pytest.mark.run(order=2)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_free_three(self, login):
        driver = login

        with allure.step("1. 点击－免费试用－立即体验，进入saas后台 断言"):
            ho.click_ele_free_trial_loc(driver, True)
            sleep(3)

            all_handles = driver.window_handles
            driver.switch_to_window(all_handles[1])
            sleep(3)

            url = driver.current_url
            assert url == 'https://admin.lifisher.com/home/workbench'

        with allure.step("2. 关闭新打开的saas后台页面"):
            driver.close()

        with allure.step("3. 窗口切回到小渔夫平台"):
            driver.switch_to_window(all_handles[0])

        with allure.step("4. 鼠标移动到：活动促销；点击－立即体验 断言"):
            ho.move_ele_event_loc(driver)
            sleep(3)
            ho.click_ele_event_promotion_loc(driver, True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/toolHome'

        with allure.step("5. 返回首页"):
            sleep(3)
            ho.click_ele_home_loc(driver, True)
            sleep(3)

        with allure.step("6. 鼠标移动到：加盟小渔夫；点击－立即体验 断言"):
            ho.move_ele_fisher_loc(driver)
            sleep(3)
            ho.click_ele_join_loc(driver, True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/about'

        with allure.step("6. 返回首页"):
            sleep(3)
            ho.click_ele_home_loc(driver, True)
            sleep(3)

    @allure.title("测试用例标题：点击－外贸学院－精选好课/Linkedin运营/外贸询盘分析&跟进技巧－立即学习－页面跳转是否正确")
    @pytest.mark.run(order=3)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_course(self, login):
        driver = login

        with allure.step("1. 页面滚动到：精选好课 点击－查看详情 断言"):
            target = ho.click_ele_course_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_course_loc(driver, True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/course/list/all'

        with allure.step("2. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

        with allure.step("3. 页面滚动到：Linkedin运营 点击－立即学习 断言"):
            target = ho.click_ele_tool_foundation_loc(driver,False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_tool_foundation_loc(driver,True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/course/contents/25'

        with allure.step("4. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

        with allure.step("5. 页面滚动到：外贸询盘分析&跟进技巧 点击－立即学习 断言"):
            target = ho.click_ele_ad_foundation_loc(driver,False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_ad_foundation_loc(driver,True)
            sleep(3)
            url = driver.current_url
            assert url == 'https://www.lifisher.com/course/contents/28'

        with allure.step("6. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

    @allure.title("测试用例标题：点击－智能云站－立即试用－页面跳转是否正确")
    @pytest.mark.run(order=4)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cloud(self, login):
        driver = login

        with allure.step("1. 页面滚动到：智能云站 点击－立即试用 进入sass后台 断言"):
            target = ho.click_ele_intelligent_cloud_station_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_intelligent_cloud_station_loc(driver, True)
            sleep(3)

            all_handles = driver.window_handles
            driver.switch_to_window(all_handles[1])
            sleep(3)

            url = driver.current_url
            assert url == 'https://admin.lifisher.com/home/workbench'

        with allure.step("2. 关闭新打开的saas后台页面"):
            driver.close()

        with allure.step("3. 窗口切回到小渔夫平台"):
            driver.switch_to_window(all_handles[0])

    @allure.title("测试用例标题：点击－智能云站－云站解决方案－查看详情－检查链接跳转是否正确")
    @pytest.mark.run(order=5)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cloud_selution(self, login):
        driver = login

        with allure.step("1. 页面滚动到：智能云站 点击－云站解决方案－查看详情 断言"):
            target = ho.click_ele_solution_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_solution_loc(driver, True)
            sleep(3)

            url = driver.current_url
            assert url == 'https://www.lifisher.com/clound'

        with allure.step("2. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

    @allure.title("测试用例标题：点击－体验版/标准版/旗舰版－立即购买－支付页面是否正确")
    @pytest.mark.run(order=6)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_standard(self, login):
        driver = login

        with allure.step("1. 页面滚动到：体验版 点击－立即购买 断言"):
            target = ho.click_ele_experience_edition_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_experience_edition_loc(driver, True)
            sleep(3)

            pay_text = oo.get_pay_text(driver)
            assert pay_text == '支付宝'

        with allure.step("2. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

        with allure.step("3. 页面滚动到：标准版 点击－立即购买 断言"):
            target = ho.click_ele_standard_edition_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_standard_edition_loc(driver, True)
            sleep(3)

            pay_text = oo.get_pay_text(driver)
            assert  pay_text == '支付宝'

        with allure.step("4. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)

        with allure.step("5. 页面滚动到：旗舰版 点击－立即购买 断言"):
            target = ho.click_ele_ultimate_loc(driver, False)
            sleep(3)
            ho.script_dowm(target, driver)
            sleep(3)
            ho.click_ele_ultimate_loc(driver, True)
            sleep(3)

            pay_text = oo.get_pay_text(driver)
            assert pay_text == '支付宝'

        with allure.step("6. 浏览器回退到上一页面：首页"):
            driver.back()
            sleep(3)







    # 第二个测试用例
    # @allure.title("测试用例标题：点击－海外营销生态服务平台－立即查看－页面跳转是否正确")
    # @pytest.mark.run(order=1)
    # @allure.tag("严重级别：高")
    # @allure.severity(allure.severity_level.CRITICAL)


    #     # 操作：点击 领英自动找客户 子页面
    #     with allure.step("3.鼠标点击：领英自动找客户 子页面"):
    #         oo.click_ele_linkdin_tab_loc(driver,True)
    #         sleep(2)
    #
    #     # 1)获取元素 2）跳转到该元素 3）操作该元素
    #     # 操作：获取 领英自动找客户 拳头页面的 "立即购买" 元素 target
    #     with allure.step("3.获取 '立即购买' 元素 target"):
    #         target = oo.click_ele_buy_linkdin_loc(driver,False)
    #         sleep(2)
    #
    #     # 操作：执行 js 脚本,跳转到指定元素上
    #     with allure.step("4.页面跳转到 '立即购买'target 且元素与底部平行"):
    #         oo.script_dowm(target,driver)
    #         sleep(3)
    #
    #     # 操作：直接点击'立即购买' target 跳转到订单页面
    #     with allure.step("5.点击 '立即购买'target 跳转到订单页面"):
    #         oo.click_ele_buy_linkdin_loc(driver,True)
    #         sleep(2)
    #
    #     # 操作：获取指定的元素值(支付方式)
    #     with allure.step("6.验证指定元素对应的值是否为支付宝"):
    #         pay_stype = oo.get_pay_text(driver)
    #
    #         # 验证指定元素值是否相等
    #         assert pay_stype =="支付宝"
    #
    #
    #
    # # 第二个测试用例
    # @allure.title("其他测试用例_002的标题：试试添加一个附件")
    # @pytest.mark.run(order=2)
    # @allure.tag("严重级别：中")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("这个用例用于验证是否可以添加一个附件")
    # def test_other_002(self):
    #     print("其他测试用例_002")
    #     allure.attach('在这个测试用例里面添加一个附件txt','C:\\Users\\Administrator\\Desktop\\代理商金额.txt',allure.attachment_type.TEXT)
    #
    # # 第三个测试用例
    # @allure.title("其他测试用例_003的标题：试试上传一张图片")
    # @pytest.mark.run(order=2)
    # @allure.tag("严重级别：低")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("这个用例用于验证是否可以上传一张图片")
    # def test_other_003(self):
    #     print("其他测试用例_003")
    #     with open(u"C:\\Users\\Administrator\\Desktop\MyTest\\picture\\53.jpg", mode='rb') as f:
    #         file = f.read()
    #         allure.attach(file, 'BUG图片', allure.attachment_type.JPG)