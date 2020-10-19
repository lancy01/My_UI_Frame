import os
import allure
from selenium import webdriver
import pytest
import time
from time import sleep

driver = None
browser_type = "Chrome"
base_url = "https://www.lifisher.com"
username = "13268023150"
password = "lancy_0216"


# 获取浏览器（驱动）
@pytest.fixture(scope='session', autouse=False)
def driver_browser():
    global driver

    if browser_type == 'Firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Ie()

    driver.maximize_window()
    driver.implicitly_wait(2)

    yield driver

    # 点击"退出" 退出登录，关闭浏览器
    driver.find_element_by_xpath('//*[@id="__layout"]/div/header/div/div/div[3]/div/div[2]').click()
    sleep(5)
    driver.close()
    driver.quit()

# 登录功能
@pytest.fixture(scope='session', autouse=False)
def login(driver_browser):
    driver = driver_browser
    driver.get(base_url)

    driver.find_element_by_xpath('//*[@id="__layout"]/div/header/div/div/div[3]/div/a[1]').click()
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="pane-second"]/form/div[1]/div/div/input').send_keys(username)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="pane-second"]/form/div[2]/div/div/input').send_keys(password)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="pane-second"]/div[1]').click()
    sleep(3)

    return driver

# 生成截图文件路径
def picture_dir():
    # 生成年月日时分秒时间
    picture_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    print(picture_time)
    print(directory_time)
    # 打印文件目录
    print(os.getcwd())

    # 获取到当前文件的目录，并检查是否有directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        file_path = '..\\..\\screen-shoots\\' + directory_time + '\\'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print("目录新建成功：%s" % file_path)
        else:
            print("目录已存在")

    except BaseException as msg:
        print("新建目录失败：%s" % msg)

    url = '..\\..\\screen-shoots\\' + directory_time + '\\' + picture_time + '.png'
    print(url)
    return url

# 保存用例失败截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to bbtain the report object
    outcome = yield
    report = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown

    if report.when == 'call' and report.failed:
        mode = 'a' if os.path.exists('failures') else 'w'

        with open('failures', mode) as f:
            # let's also access a fixture for the fun of it
            if 'tmpdir' in item.fixturenames:
                extra = '(%s)' % item.funcargs['tmpdir']
            else:
                extra = ''
            f.write(report.nodeid + extra + '/n')

        # pic_info = adb_screen_shot()
        with allure.step('添加失败步骤截图~~~'):
            url = picture_dir()
            print(url)
            driver.get_screenshot_as_file(url)

            allure.attach.file(url, '失败截图：{filename}'.format(filename=url), allure.attachment_type.PNG)




