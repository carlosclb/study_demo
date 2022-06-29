# 读一行
# 参数解读：get_row(excel的路径，选择的子表格名字，所读行的位置)
import xlrd


def get_row(file_path, subtable, row_location):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(subtable)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    # 获取选取对象的行列值
    row_num = sheet.nrows
    colNum = sheet.ncols
    # 获取某一行的数据
    row_location_value = sheet.row_values(row_location)
    # 返回的结果为列表，例如：[1，2，3，4]
    return row_location_value


# 读多行数据
# 参数解读：get_rows(excel的路径，选择的子表格名字，所读行开始的位置，所读行结束的位置)
def get_rows(file_path, subtable, start, end):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(subtable)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    # 获取多行数据
    value_library = []
    for row_location in range(int(start), int(end) + 1):
        row_location_value = sheet.row_values(row_location)
        value_library.append(row_location_value)
    return value_library


# 读全部数据
# 参数解读：get_all(excel的路径，选择的子表格名字)
def get_all(file_path, subtable):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(subtable)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    # 获取选取对象的行数
    row_num = sheet.nrows
    value_library = []
    for row_location in range(row_num):
        row_location_value = sheet.row_values(row_location)
        value_library.append(row_location_value)
    return value_library


# 读一列
# 参数解读：get_col(excel的路径，选择的子表格名字，读列的位置)
def get_col(file_path, sheet_name, local):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(sheet_name)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    cols = sheet.col_values(local)
    return cols


# 读多列
# 参数解读：get_cols(excel的路径，选择的子表格名字，读列开始的位置，读列结束的位置)
def get_cols(file_path, sheet_name, start, end):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(sheet_name)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    final_result = []
    for i in range(start, end + 1):
        cols = sheet.col_values(i)
        final_result.append(cols)
    return final_result


if __name__ == '__main__':
    print(get_row(r"2.xlsx", "sheet1", 1))  # 读一行
    print(get_rows(r"2.xlsx", "sheet1", 1, 3))  # 读多行
    print(get_all(r"2.xlsx", "sheet1"))  # 读全部数据
    print(get_col(r"2.xlsx", "sheet1", 1))  # 读一列
    print(get_cols("111.xlsx", "sheet1", 1, 3))  # 读多列
