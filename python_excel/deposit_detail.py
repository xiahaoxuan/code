import xlrd
import pandas as pd

workbook = xlrd.open_workbook("充值信息.xls")

sheet = workbook.sheet_by_index(0)

# 获取这个sheet中的行数和列数
nrows = sheet.nrows
ncols = sheet.ncols
people_list = []
money_list = []
for index in range(0, sheet.nrows):
    temp = {}
    if index > 0:
        cells = sheet.row_slice(index, 0, 15)
        if cells[1].value not in people_list:
            money = float(cells[7].value) + float(cells[8].value) - float(cells[10].value) - float(
                cells[11].value) + float(cells[12].value)
            temp["name"] = cells[1].value
            temp["number"] = cells[2].value
            temp["id_number"] = cells[4].value.replace('C', 'G')
            temp["money"] = money
            money_list.append(temp)
            people_list.append(temp["name"])
        else:
            for dict_money in money_list:
                if cells[1].value == dict_money["name"]:
                    money = float(cells[7].value) + float(cells[8].value) - float(cells[10].value) - float(
                        cells[11].value) + float(cells[12].value) + dict_money["money"]
                    dict_money["money"] = money
print("开卡总人数{}".format(len(people_list)))


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
        'money': '充值金额',
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    # is_path = os.path.exists('index_before.xlsx')
    file_path = pd.ExcelWriter("整理后充值信息.xls")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


export_excel(money_list)
