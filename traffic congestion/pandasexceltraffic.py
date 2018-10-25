
import xlrd
data = xlrd.open_workbook('F:/7gaodetraffic/13functionCONGESTION/FZidenzone.xlsx')
table = data.sheets()[1]
b = table.nrows #行数
#print(nrows)
rowslist=[]
sheet_names= data.sheet_names()
sheet2 = data.sheet_by_name('Sheet1')
for a in range(1,b):
#print(a)
    rows = sheet2.row_values(a)
    #print(rows)
    rowslist.append(rows)
print(rowslist)

