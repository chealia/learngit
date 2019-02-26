# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:43:28 2018

@author: chealia
"""

import xlrd
from  xlutils.copy import copy
from xml.parsers.expat import ParserCreate

rb=xlrd.open_workbook(r'c:\users\chealia\201812\drug.xlsx')
wb=copy(rb)
global i
i=0
global j
j=0
global flag
flag=0
c1=wb.get_sheet(0)

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        global i  #全局变量在使用前还要再声明一次，切记！
        global flag
        global j
        if i>65535:
            return
        if name=='drug' and flag==0:
            c1.write(i,0,attrs.get('type'))
            flag=0
            j=i #第j行就是第i行
            i=i+1 
            
        if name=='drugbank-id' and flag==0:            
            flag=1
        if name=='name' and flag==10:
            flag=2
        if name=='description' and flag==0:            
            flag=3
        if name=='groups' and flag==0:
            flag=4
        if name=='group' and flag==4:
            flag=41
        if name=='indication' and flag==0:
            flag=5
        if name=='products' and flag==6:
            flag=61
        if name=='name' and flag==61: #产品内的详细信息
            flag=62
        if name=='pathways' and flag==7:#products之后还有pathways里会出现<drug>
            flag=8
            
    def end_element(self,name):
        global flag
        if name=='drugbank-id' and flag==1:
            flag=10 #drugbank-id之后恢复
        if name=='name' and flag==2:
            flag=0
        if name=='description' and flag==3:            
            flag=0
        if name=='group' and flag==41:
            flag=0
        if name=='indication' and flag==5:
            flag=6
        if name=='name' and flag==62: 
            flag=7
        if name=='products' and flag==61: #如果有产品但是没有name，flag终结于7
            flag=7
        if name=='pathways' and flag==8:
            flag=9
        if name=='drug' and flag==9:
            flag=0
    def char_data(self,text):
        global flag
        if flag==1:
            c1.write(j,1,text)
        if flag==2:
            c1.write(j,2,text)
        if flag==3:
            c1.write(j,3,text)
            
        if flag==41:
            c1.write(j,4,text)
        if flag==5:   #5是适应症
            c1.write(j,5,text)
        if flag==62:
            c1.write(j,6,text)
            print('sax:char_data:%s'%text)
        
            



with open(r'c:\users\chealia\201812\full database2.xml','r',encoding='utf-8') as f:
    xml=f.read()
print(type(xml))
handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)
wb.save(r'c:\users\chealia\201812\drug.xls')