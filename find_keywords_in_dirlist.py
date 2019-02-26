# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:27:32 2018

@author: chealia
"""


import os
def find(keywords,path=os.path.abspath('.')):
    
    for x in os.listdir(path) :
        #p=os.path.join(path,x)
        if os.path.isfile(x) and os.path.splitext(x)[0].find(keywords)!=-1:
            #print(p)
            print(os.path.splitext(x)[0])
            print('Find file:%s,Path:%s'%(x,path))
            
        elif os.path.isdir(x):
            try:
                find(keywords,os.path.join(path,x))
            except PermissionError:
                pass
    return
find('untitled',r'c:\users\chealia')

