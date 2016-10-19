# Python script to convert Excel file to csv File
import xlrd
import csv
from os import sys
from collections import OrderedDict

def convertExcel2cvs(excel_file):

    wb = xlrd.open_workbook(excel_file)
    sh = wb.sheet_by_index(0)
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
         wr.writerow(
             list(x.encode('utf-8') if type(x) == type(u'') else x
                  for x in sh.row_values(rownum)))

if __name__ == "__main__":
    convertExcel2cvs(sys.argv[1])
