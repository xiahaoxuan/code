import xlrd

workbook = xlrd.open_workbook("充值信息.xls")

sheet = workbook.sheet_by_index(0)

# 获取这个sheet中的行数和列数
nrows = sheet.nrows
ncols = sheet.ncols
people_list = []
for index in range(0, sheet.nrows):
    temp = {}
    if index > 0:
        cells = sheet.row_slice(index, 0, 15)
        student_number = cells[2].value
        people_list.append(student_number)

people_set = set(people_list)
print("开卡总人数{}".format(len(people_set)))
