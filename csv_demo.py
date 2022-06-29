import csv


def first_type():
    headers = ['学号', '姓名', '分数']
    rows = [('202001', '张三', '98'), ('202002', '李四', '95'), ('202003', '王五', '92')]
    # rows = [['202001', '张三', '98'], ['202002', '李四', '95'], ['202003', '王五', '92']]
    with open('score1.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def second_type():
    headers = ['学号', '姓名', '分数']
    rows = [{'学号': '202001', '姓名': '张三', '分数': '98'},
            {'学号': '202002', '姓名': '李四', '分数': '95'},
            {'学号': '202003', '姓名': '王五', '分数': '92'}]
    with open('score2.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(rows)


def third_type():
    headers = ['学号,姓名,分数', '\n']
    rows = ['202001,张三,98', '\n',
            '202002,李四,95', '\n',
            '202003,王五,92']
    with open('score3.csv', 'w', encoding='utf8', newline='') as f:
        f.writelines(headers)  # write() argument must be str, not tuple
        f.writelines(rows)


def read_csv1():
    # 读取csv文件
    with open('score1.csv', "r", encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(type(row), row)


def read_csv2():
    # 读取csv文件
    with open('score1.csv', "r", encoding='utf8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(type(row), row)


first_type()  # 写csv文件，方式一
second_type()  # 写csv文件，方式二
third_type()  # 写csv文件，方式三

read_csv1()
read_csv2()
