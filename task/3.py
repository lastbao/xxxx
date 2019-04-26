import xlrd
import xlwt
wb = xlrd.open_workbook('C://Users//10579//Desktop//gg.xlsx')
myWorkbook = xlwt.Workbook()
mySheet = myWorkbook.add_sheet('A Test Sheet')
sheet_name = wb.sheet_names()[0]
sheet = wb.sheet_by_index(0)
dic = [[]for i in range(sheet.nrows-1)]
print(sheet.nrows)
print(sheet.ncols)
for i in range(sheet.nrows-1):
        for j in range(1,2):
                dic[i].append(sheet.cell(i+1,j).value)
print(dic[0])
for i in range(sheet.nrows-1):                
        mySheet.write(i//11,i%11,dic[i])                                    
myWorkbook.save('C://Users//10579//Desktop//dd.xls')