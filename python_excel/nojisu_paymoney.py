import xlrd
import pandas as pd

workbook = xlrd.open_workbook("整理后充值信息.xls")

sheet = workbook.sheet_by_index(0)

pay_list = []
for index in range(1, sheet.nrows):
    temp = {}
    cell = sheet.row_slice(index, 0, 4)
    temp["name"] = cell[0].value
    temp["number"] = cell[1].value
    temp["id_number"] = cell[2].value
    temp["money"] = cell[3].value
    pay_list.append(temp)

print('充值人数{}'.format(len(pay_list)))

workbook_1 = xlrd.open_workbook("整理后寄宿明细信息.xls")

sheet_1 = workbook_1.sheet_by_index(0)

people_list = []
for index in range(1, sheet_1.nrows):
    cell = sheet_1.row_slice(index, 0, 3)
    people_list.append(cell[2].value)

print('寄宿人数{}'.format(len(people_list)))
not_pay_list = []
for pay in pay_list:
    if pay["name"] not in people_list:
        not_pay_list.append(pay)
print('未寄宿充值人数{}'.format(len(not_pay_list)))


def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['name', 'number', 'id_number', 'money']
    pf = pf[order]
    # 将列名替换为中文
    columns_map = {
        'name': '姓名',
        'number': '电子卡号',
        'id_number': '证件号码',
        'money': '充值金额'

    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    # is_path = os.path.exists('index_before.xlsx')
    file_path = pd.ExcelWriter("未寄宿充值名单信息.xls")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


export_excel(not_pay_list)
