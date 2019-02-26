# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:44:11 2018

@author: chealia
"""



import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

rb=open_workbook(r'c:/users/chealia/zhongliu/drugbank.xlsx')
wb=copy(rb)
s1=rb.sheet_by_index(0)
s2=wb.get_sheet(0)
print(s1.nrows)

if __name__=='__main__':
    r=0
    for i in range(s1.nrows):
        cl=s1.cell_value(i,1)
        cls=cl.split(' | ')
        for x in cls:
            print(x)
            s2.write(r,0,s1.cell_value(i,0))
            s2.write(r,1,x)
            r=r+1
        wb.save(r'c:/users/chealia/zhongliu/drugbank2.xls')