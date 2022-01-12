import xlrd
import pandas as pd

workbook = xlrd.open_workbook("2021年下学期学生缴费明细表.xls")

sheet = workbook.sheet_by_index(0)
people_list = []
grade = ""
for index in range(0, sheet.nrows):
    temp = {}
    cells = sheet.row_slice(index, 0, 15)
    cell = str(cells[10].value)
    if len(cell) == 10:
        if cells[4].value:
            grade = cells[4].value
        temp["grade"] = grade
        temp["number"] = "G" + str(grade[-6:-4]) + str(grade[-3:-1])
        temp["name"] = cells[-1].value
        people_list.append(temp)

print("寄宿总人数是{}".format(len(people_list)))


def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['grade', 'number', 'name']
    pf = pf[order]
    # 将列名替换为中文
    columns_map = {
        'grade': '班级',
        'number': '证件号码',
        'name': '姓名',
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    # is_path = os.path.exists('index_before.xlsx')
    file_path = pd.ExcelWriter("整理后寄宿明细信息.xls")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


export_excel(people_list)
