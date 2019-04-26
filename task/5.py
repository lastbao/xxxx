import xlrd
import xlwt
import re
import json
wb = xlrd.open_workbook('C://Users//10579//Desktop//xx.xls')
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
pattern = re.compile(r'[A-Z]+')
while i<len(dic):
        j = 0
        while j<len(dic[i]):
                if ((pattern.findall(dic[i][6])!=['M'])or(dic[i][7]!='星期1')) and ((pattern.findall(dic[i][6])!=['N'])or(dic[i][7]!='星期1')):
                      dic.pop(i)
                      i -= 1
                j += 1
        i += 1
pattern2 = re.compile(r'\d+')
i=0 
while i<len(dic):
        j = 0
        while j<len(dic[i]):
                count3 =0
                count4 =0
                flag1 = False    
                for k in pattern2.findall(dic[i][9]):
                        if(int(k)<8):
                                count3+=1
                        if(int(k)>8):
                                count4+=1
                        if(int(k)==8):
                                flag1 = True
                if((count3%2==0)and(count4%2==0)and(not flag1))or((count3+count4==1)):
                        dic.pop(i) 
                        i -= 1
                j += 1
        i += 1
for i, element_i in enumerate(dic):
        for j, element_j in enumerate(element_i):
                mySheet.write(i,j,dic[i][j])
myWorkbook.save('C://Users//10579//Desktop//qq.xls')
pattern3 =re.compile(r'\d+|[A-Z]+')
p=[]
for i, element_i in enumerate(dic):
        string1=(pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1]
        p.append(string1)
diction={}
p=list(set(p))
p.sort()
for g,element_g in enumerate(p):
        count5=True
        count6=True
        count7=True
        count8=True
        count9=0
        for i, element_i in enumerate(dic):
                penny=[]
                string2=(pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1]
                if(dic[i][8]=='第1大节')and(((pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1])==p[g]):
                        count5=False
                if(dic[i][8]=='第2大节')and(((pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1])==p[g]):
                        count6=False
                if(dic[i][8]=='第3大节')and(((pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1])==p[g]):
                        count7=False
                if(dic[i][8]=='第4大节')and(((pattern3.findall(dic[i][6]))[0]+(pattern3.findall(dic[i][6]))[1])==p[g]):
                        count8=False
        penny.append(count5)
        penny.append(count6)
        penny.append(count7)
        penny.append(count8)
        penny.append(True)
        penny.append(True)
        diction.setdefault(p[g],penny)
json_str =json.dumps(diction,indent=4)
with open ('C://Users//10579//Desktop//xx.json','w') as json_file:
        json_file.write(json_str)



