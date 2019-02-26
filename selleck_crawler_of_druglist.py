# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:44:11 2018

@author: chealia
"""



import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
from lxml import etree
import requests


rb=open_workbook(r'c:/users/chealia/xxx.xlsx')
wb=copy(rb)
s1=rb.sheet_by_index(0)
s2=wb.get_sheet(0)
print(s1.nrows)

if __name__=='__main__':
    r=0
    l=[]
    for i in range(s1.nrows):
        cl=s1.cell_value(i,0)
        url='https://www.selleck.cn/products/%s.html'%(cl)
        l.append(url)
        s2.write(r,2,url)
        r=r+1

    t=0
    for url in l:
        data=requests.get(url).text
        s=etree.HTML(data)
        des=s.xpath('//*[@id="selectTotal"]/p//text()')
        s2.write(t,3,des)
        t=t+1
        wb.save(r'c:/users/chealia/xxx.xls')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        