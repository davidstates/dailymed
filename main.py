import xlrd
import re
from operator import itemgetter

file_name = 'druglist.xlsx'

wb = xlrd.open_workbook(filename=file_name)

indication = {}

for sheet in wb.sheets():
    nrow = sheet.nrows
    disease = sheet.name
    for ic in range(0, nrow):
        row = sheet.row_values(ic)[0]
        if ic>0 and re.match('^NDC Code', row):
            id = ic-1
            drugname = sheet.cell_value(id, 0)
            drug = re.match('([A-Z0-9]+)', drugname)[0]
            if drug not in indication.keys():
                indication[drug] = {disease : 1}
            else:
                if disease not in indication[drug].keys():
                    indication[drug][disease] = 1
                else:
                    indication[drug][disease] += 1

for drug in sorted(indication.keys()):
    print(drug + ": " + ", ".join(sorted(indication[drug].keys())))

