import xlrd
import xlwt
wb = xlrd.open_workbook('C://Users//10579//Desktop//dd.xls')
myWorkbook = xlwt.Workbook()
mySheet = myWorkbook.add_sheet('A Test Sheet')
sheet_name = wb.sheet_names()[0]
sheet = wb.sheet_by_index(0)
dic = [[]for i in range(sheet.nrows-1)]
print(sheet.nrows)
print(sheet.ncols)
for i in range(sheet.nrows-1):
        for j in range(sheet.ncols):
                dic[i].append(sheet.cell(i,j).value)
count = 0
i = 0
while i<len(dic):
        j = 0
        while j<len(dic[i]):
                if(dic[i][j].strip()==''):
                      dic.pop(i)
                      i -= 1
                j += 1
        i += 1

for i, element_i in enumerate(dic):
        for j, element_j in enumerate(element_i):
                mySheet.write(i,j,dic[i][j])
myWorkbook.save('C://Users//10579//Desktop//xx.xls')


