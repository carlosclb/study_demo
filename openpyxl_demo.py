from openpyxl import load_workbook

wb = load_workbook('2.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]

# 获取第一行所有数据
row1 = []
for row in sheet1[1]:
    row1.append(row.value)
# print(row1)

# 获取第一列所有数据
col1 = []
for col in sheet1['A']:
    col1.append(col.value)
# print(col1)

rows = sheet1.rows
columns = sheet1.columns

# 迭代读取所有的行
for row in rows:
    row_val = [col.value for col in row]
    print(row_val)
print('')

# 迭代读取所有的列
for col in columns:
    col_val = [row.value for row in col]
    print(col_val)