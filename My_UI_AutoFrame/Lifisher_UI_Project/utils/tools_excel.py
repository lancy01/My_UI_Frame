#!/usr/bin/python3

"""
@author: ysw
@contact: ysw@gzwison.com
@software: PyCharm
@file: tools_excel.py
@time: 2020/4/3 14:15
@DESC:
"""

import os
import xlrd

"""
XlsxWriter：写excel文件
1：创建Excel：xl = xlsxwriter.Workbook('test.xls')；
2：添加sheet：table = xl.add_worksheet('sheet1')；
3：写单元格：table.write_string(0, 0, 'first')/('A1', 'first')
4：设置单元格大小：table.set_column('C:E', 15)；
5：Excel关闭：xl.close()；

xlsxwriter模块写入格式：
write_boolean  写boolean 值
write_datetime 写日期
write_number 写数字
write_string 写字符串
write_blank 空
write_url 写连接
write_formula 写公式
insert_image 插入图片
merge_range 合并单元格写入

xlsxwriter单元格格式：add_format
color ：red 颜色
num_format:yy-mm-dd 日期格式
url:www.baidu.com 超链接
bold:True 加粗
font_size：12 字体设置
underline：True 下划线设置
bg_color:red 单元格颜色

xlrd模块读取excel内容：
1：xl = xlrd.open_workbook('test.xls')：打开excel
2：table =xl.sheets()[0]：通过索引获取工作表
3：row = table.row_values(0)：获取第一行内容
4：col = table.col_values(0)：获取第一列整列内容
5：table.nrwos：行数，table.ncols：列数
6：table.cell(0,0).value：单元格值
excel表格单元类型：
0 空
1 str
2 num
3 data
4 boolean
5 error

"""
def tool_excel(url, sheetname):
    # 首先拿到book对象
    book = xlrd.open_workbook(url)
    sheet_by_name = book.sheet_by_name(sheetname)

    # 获取行数
    rows = sheet_by_name.nrows
    print("打印获取到的行数:"+str(rows))

    # 获取列数
    cols = sheet_by_name.ncols
    print("打印获取到的列数:"+str(cols))

    # 读取每行的内容
    for row in range(rows):
        # 使用 row方法读取
        # print(sheet_by_name.row(row))
        # 也可以使用row_values读取
        print('rows')
        print(sheet_by_name.row_values(row))

    # 读取每列的内容
    for col in range(cols):
        # 下面两种方法都可以
        # print(sheet_by_name.col(col))
        print('cols')
        print(sheet_by_name.col_values(col))

    # 读取固定列的内容
    print('固定列')
    # cell(1,1)第二行第二列内容
    print(sheet_by_name.cell(1, 1))
    print('固定列内容')
    # cell_value(1, 2)第二行第三列内容
    print(sheet_by_name.cell_value(1, 2))

    # 将每行都和首行组成字典，存放在一个列表中
    l = []
    # 获取首行列内容
    title = sheet_by_name.row_values(0)
    # print(title)
    # range(2, rows)第三行开始，到
    for row in range(2, rows):
        l.append(dict(zip(title, sheet_by_name.row_values(row))))
    print("组合列名和列内容")
    print(l)


if __name__ == "__main__":
    tool_excel('../data/parametrize_test_case.xlsx', '参数化')
