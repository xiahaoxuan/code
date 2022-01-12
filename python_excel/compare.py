import xlrd
import pandas as pd

workbook = xlrd.open_workbook("整理后充值信息.xls")

sheet = workbook.sheet_by_index(0)

pay_list = []
for index in range(1, sheet.nrows):
    cell = sheet.row_slice(index, 0, 4)
    pay_list.append(cell[0].value)

print('充值人数{}'.format(len(pay_list)))

workbook_1 = xlrd.open_workbook("整理后寄宿明细信息.xls")

sheet_1 = workbook_1.sheet_by_index(0)

people_list = []
for index in range(1, sheet_1.nrows):
    temp = {}
    cell = sheet_1.row_slice(index, 0, 3)
    temp["grade"] = cell[0].value
    temp["id_number"] = cell[1].value
    temp["name"] = cell[2].value
    people_list.append(temp)

print('寄宿人数{}'.format(len(people_list)))
not_pay_list = []
for people in people_list:
    if people["name"] not in pay_list:
        not_pay_list.append(people)
print('未充值{}'.format(len(not_pay_list)))


def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['grade', 'id_number', 'name']
    pf = pf[order]
    # 将列名替换为中文
    columns_map = {
        'grade': '班级',
        'id_number': '证件号码',
        'name': '姓名',
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    # is_path = os.path.exists('index_before.xlsx')
    file_path = pd.ExcelWriter("未充值名单信息.xls")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


export_excel(not_pay_list)
