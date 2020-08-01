import os
from time import sleep
import pytest
import allure
from Lifisher_UI_Project.src.base_operate.order_operate import OrderOperate

@allure.epic("小渔夫建站工具订购大模块")
@allure.feature("po登录特性模块")
# 业务层 继承 操作层
class TestCaseLinder(OrderOperate):

    # 第一个测试用例
    @allure.title("测试用例标题：自动登录并下单购买领英工具")
    @pytest.mark.run(order=1)
    @allure.tag("严重级别：高")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("这个用例用于验证下单功能是否正常")
    def test_login_lifisher(self, login, log_record):

        # 实例化 操作层(OrderOperate)对象
        oo = OrderOperate()
        driver = login
        logger = log_record

        page_title = "小渔夫 - 外贸营销综合平台 - 企业出海，找小渔夫"

        # 调用打开页面组件
        with allure.step("1.验证测试的网页是否打开正确"):
            oo.open(driver,page_title)

        # 操作：点击登录后的 "领英自动找客户" tab元素
        with allure.step("2.登录成功后，点击 领英自动找客户 tab 元素"):
            oo.click_ele_linder_tab_loc(driver)
            driver.implicitly_wait(10)
            sleep(2)

        # 1)获取元素 2）跳转到该元素 3）操作该元素
        # 操作：获取 领英自动找客户 拳头页面的 "立即购买" 元素 target
        with allure.step("3.获取 '立即购买' 元素 target"):
            target = oo.click_ele_buy_linder_loc(driver,False)

        # 操作：执行 js 脚本,跳转到指定元素上
        with allure.step("4.页面跳转到 '立即购买'target 且元素与底部平行"):
            oo.script_dowm(target,driver)

        # 操作：直接点击'立即购买' target 跳转到订单页面
        with allure.step("5.点击 '立即购买'target 跳转到订单页面"):
            oo.click_ele_buy_linder_loc(driver,True)

        # 操作：获取指定的元素值(支付方式)
        with allure.step("6.验证指定元素对应的值是否为支付宝"):
            pay_stype = oo.get_pay_text(driver)

            # 验证指定元素值是否相等
            assert pay_stype =="微信"

            logger.debug('debug message')
            logger.info('info message')
            logger.warning('warning message')
            logger.error('error message')
            logger.critical('critical message')

    # 第二个测试用例
    @allure.title("其他测试用例_002的标题：试试添加一个附件")
    @pytest.mark.run(order=2)
    @allure.tag("严重级别：中")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("这个用例用于验证是否可以添加一个附件")
    def test_other_002(self):
        print("其他测试用例_002")
        allure.attach('在这个测试用例里面添加一个附件txt','C:\\Users\\Administrator\\Desktop\\代理商金额.txt',allure.attachment_type.TEXT)

    # 第三个测试用例
    @allure.title("其他测试用例_003的标题：试试上传一张图片")
    @pytest.mark.run(order=2)
    @allure.tag("严重级别：低")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("这个用例用于验证是否可以上传一张图片")
    def test_other_003(self):
        print("其他测试用例_003")
        with open(u"C:\\Users\\Administrator\\Desktop\MyTest\\picture\\53.jpg", mode='rb') as f:
            file = f.read()
            allure.attach(file, 'BUG图片', allure.attachment_type.JPG)





if __name__ == '__main__':
    pytest.main(["test_order.py"])
    os.system("allure generate ../../../report-results/ -o ../../../allure-report --clean")

