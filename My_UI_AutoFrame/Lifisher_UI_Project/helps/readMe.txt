allure-logs     —— 自动化测试执行相关日志
allure-report   —— 自动化测试执行结果可视化报告
conf            ——配置文件目录，主要是log日志配置
data            ——三方数据存储目录
driver          —— 存放浏览器驱动
helps           ——资料帮助文档
report-results  ——存放自动化测试结果数据
screen-shoots   ——存放异常测试截图

src ——
    |___ base_common         —— 定义预操作，用于被继承或者重新封装
    |___ base_object         —— 定义页面基础类，封装所有页面元素公用的方法，对象层
    |___ base_operate        —— 定义页面的基本操作方法，操作层
    |
    |___ test_suite               —— 测试用例集
    |       |___test_1_case       —— 具体测试用例，业务层,第一个数字对应page_object.base_page_1_1_page.py
    |       |                            的第一个数字
    |       |___test_2_case       —— 具体测试用例，业务层，同上
    |
    |___ test_temp_case           —— 临时用例文件夹

utils —— 存放一些公用的PY文件

conftest.py                         ——配置文件，提示日志容器
pytest.ini                          ——项目配置文件，可修改pytest命令默认行为
environment.properties              ——测试报告展示环境属性文件
categories.json                     ——测试异常类别json配置文件
