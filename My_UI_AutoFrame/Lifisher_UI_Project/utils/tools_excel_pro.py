import os
import xlrd

"""
XlsxWriter：写excel文件
1：创建Excel：xl = xlsxwriter.Workbook('test.xls')
2：添加sheet：table = xl.add_worksheet('sheet1')
3：写单元格：table.write_string(0, 0, 'first')/('A1', 'first')
4：设置单元格大小：table.set_column('C:E', 15)
5：Excel关闭：xl.close()

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
    book = xlrd.open_workbook(url, formatting_info=False)
    table = book.sheet_by_name(sheetname)

    # 获取行数
    rows = table.nrows
    print("打印获取到的行数:"+str(rows)+'行')

    # 获取列数
    cols = table.ncols
    print("打印获取到的列数:"+str(cols)+'列')

    # 读取每行的内容
    for row in range(rows):
        print('rows',rows)
        print(table.row_values(row))

    # 读取每列的内容
    for col in range(cols):
        print('cols',cols)
        print(table.col_values(col))

    # 读取固定列的内容
    print('固定列')
    print(table.cell(0, 0)) # cell(1,1)第二行第二列内容

    print('固定列内容')
    print(table.cell_value(1, 1)) # cell_value(1, 2)第二行第三列内容

    print('= '* 50)

    # 将每行都和首行组成字典，存放在一个列表中
    L = []
    # 获取首行内容
    title = table.row_values(0)
    print('title',title)

    for row in range(1, rows):
        print('每一行的值',table.row_values(row))
        L.append(dict(zip(title, table.row_values(row))))
    print(L)

    print('= ' * 50)

    # 表的获取方法
    table_01 = book.sheets()[0]
    table_02 = book.sheet_by_index(0)
    table_03 = book.sheet_by_name('参数化1')
    print(table_01,table_02,table_03)

    print('= ' * 50)

    names = book.sheet_names() # 返回book中所有工作表的名字

    print('= ' * 50)

    print(book.sheet_loaded('参数化1')) # 检查某个sheet是否导入完毕

    print('= ' * 50)

    # 行的操作
    nrows = table.nrows # 获取该sheet中的有效行数

    a = table.row(1) # 返回由该行中所有的单元格对象组成的列表
    b = table.row_slice(2) # 返回由该行中所有的单元格对象组成的列表
    c = table.row_types(1, start_colx=0, end_colx=None) # 返回由该行中所有单元格的数据类型组成的列表
    d = table.row_values(1, start_colx=0, end_colx=None) # 返回由该行中所有单元格的数据组成的列表

    e = table.row_len(1) # 返回该列的有效单元格长度

    print('= ' * 50)

    # 列的操作
    ncols = table.nrows # 获取列表的有儿列数

    f = table.col(1, start_rowx=0, end_rowx=None) # 返回由该列中所有的单元格对象组成的列表
    g = table.col_slice(1, start_rowx=0, end_rowx=None) # 返回由该列中所有的单元格对象组成的列表
    h = table.col_types(1, start_rowx=0, end_rowx=None) # 返回由该列中所有单元格的数据类型组成的列表
    i = table.col_values(1, start_rowx=0, end_rowx=None) # 返回由该列中所有单元格的数据组成的列表

    print('= ' * 50)

    # 单元格的操作
    aa = table.cell(1,1) # 返回单元格对象
    bb = table.cell_type(1,1) # 返回单元格中的数据类型
    cc = table.cell_value(1,1) # 返回单元各中的数据
    print('aa',aa,'bb',bb,'cc',cc)




if __name__ == "__main__":
    excel_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              '../data/parametrize_test_login.xls'))
    print(excel_path)
    tool_excel(excel_path,'参数化1')

