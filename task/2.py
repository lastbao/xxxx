import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys
import os
response = requests.get("http://today.hitwh.edu.cn/2018/1119/c1026a100732/page.htm")
response.encoding ="utf-8"
soup = BeautifulSoup(response.text,'lxml')
f=open("C://Users//10579//Desktop//1.txt","w")
list1=[]
string1=""
pattern4 = re.compile(r'[\u4e00-\u9fa5]')
pattern5 = re.compile(r'[\u4e00-\u9fa5a-zA-Z0-9]')
string2=str(soup.find_all("title"))
for item in pattern4.findall(string2):
    string1=string1+item
f.write(string1)
string3=str(soup("meta"))
string4=""
for item in pattern4.findall(string3):
    string4=string4+item
f.write("\n")
f.write(string4)   
string5=str(soup.find_all(attrs={"class":"newsNav"}))
f.write("\n")
f.write(string5)
link2st=[]
for x in soup.find_all('img', src = re.compile('/_upload/article/images')):
    link = x.get('src')
    if link:
        link2st.append(link)
link2st=list(set(link2st))
for x in link2st:
    f.write("\n")
    f.write(x)
linklst = []
for x in soup.find_all('a', href = re.compile('2019/0426')):
    link = x.get('href')
    if link:
        linklst.append(link)
linklst=list(set(linklst))
for x in linklst:
    f.write("\n")
    f.write(x)
f.close()

