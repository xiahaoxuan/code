import xlrd

workbook = xlrd.open_workbook("充值信息.xls")
sheet_names = workbook.sheet_names()
sheets = workbook.sheets()
for sheet in sheets:
    for col in range(sheet.ncols):
        for row in range(sheet.nrows):
            cell = sheet.cell(row, col)
            if cell.value:
                sheet_names.append(str(cell.value))
sheet_content = " ".join(sheet_names)
# total = 10000000000
# used = 333333337
#
# memory = round(used/total, 2)
# memory = "%s%%" % (memory * 100)
# print(memory)
