__author__ = 'Andrei Pervychine'
import sys
import xlrd
import csv

def export_xlsx_file(filepath):
    wb = xlrd.open_workbook(filepath)

    for i in range(0, wb.nsheets):

        sh = wb.sheet_by_index(i)
        sheet_name = sh.name
        sheet_name = sheet_name.replace(" ", "_");
        fp = open(sheet_name+'.csv', 'at', encoding='utf8')
        wr = csv.writer(fp, quoting=csv.QUOTE_ALL)

        for row_num in range(sh.nrows):
            wr.writerow(sh.row_values(row_num))

        fp.close()

## getting arguments passed ##
if len(sys.argv) > 1:
    file = sys.argv[1]
    export_xlsx_file(file)
    print("file successfully exported")
else:
    print("please pass the filename as a parameter")
