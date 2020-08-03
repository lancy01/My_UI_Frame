import os
import xlrd

"""
xlrd模块读取excel内容：
1：xl = xlrd.open_workbook('test.xls')：打开excel
2：table =xl.sheets()[0]：通过索引获取工作表
3：row = table.row_values(0)：获取第一行内容
4：col = table.col_values(0)：获取第一列整列内容
5：table.nrwos：行数，table.ncols：列数
6：table.cell(0,0).value：单元格值
excel表格单元类型：
0 空 1 str 2 num 3 data 4 boolean 5 error

"""

def tool_excel(excel_path, sheet_name):
    # 获取工作簿
    book = xlrd.open_workbook(excel_path, formatting_info=False)
    # 根据工作簿获取工作表
    table = book.sheet_by_name(sheet_name)

    # 获取行数
    rows = table.nrows

    # 获取列表
    cols = table.ncols

    param = []
    case = []

    # 读取每行的内容
    for row in range(rows):
        print('rows',rows)
        print(table.row_values(row))

    # 获取每列的内容
    for col in range(cols):
        print('cols',cols)
        print(table.col_values(col))

    for i in range(1, rows):

        for j in range(0,cols):
            case.append(table.cell_value(i, j))

        param.append(tuple(case))
        case = []

    return param

if __name__ == '__main__':
    excel_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              '../data/parametrize_test_login.xls'))
    print(excel_path)
    param = tool_excel(excel_path, '参数化1')
    print(param)

