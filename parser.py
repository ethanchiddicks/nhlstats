from xlrd import open_workbook, cellname
import os

myFilename = os.path.normpath("C:/Users/ethan_000/Desktop/NHL Stats/NHL 2011-12.xls")
book = open_workbook(myFilename)

#for s in wb.sheets():
#    print('Sheet:', s.name)
#    for row in range(s.nrows):
#        values = []
#        for col in range(s.ncols):
#            values.append(s.cell(row,col).value)
#        print(','.join(values))
#    print
    
print(book.sheet_names())

sheet = book.sheet_by_index(0)

print(sheet.name)

print(sheet.nrows)
print(sheet.ncols)

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print(cellname(row_index,col_index),'-',)
        print(sheet.cell(row_index,col_index).value)