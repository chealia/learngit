# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:38:37 2018

@author: chealia
"""

import xlrd,requests,re
from lxml import etree
links=[]

l=[0]
for i in range(97,122):
    l.append(chr(i))
for i in l:
    url='https://ghr.nlm.nih.gov/condition?initial=%s'%(i)
    data=requests.get(url).text
    s=etree.HTML(data)
    link=s.xpath('//*[@id="skip"]/div/div/div/section/ul/li/a/@href')
    for l1 in link:
        if l1 not in links:
            links.append(l1)
for l2 in links:
    url='https://ghr.nlm.nih.gov%s'%(l2)
    data=requests.get(url).text
    s=etree.HTML(data)    
    name=s.xpath('//*[@id="skip"]/div/div[1]/div/section/div[1]/h1/text()')[0]
    print(name)
    add_reso=s.xpath('//*[@id="resources"]//@href')
    omim=[]
    for i in  add_reso:
        if re.match(r'^(http://omim.org/entry/)(\d*)$',i):
            m=re.match(r'^(http://omim.org/entry/)(\d*)$',i)
            omim.append(m.group(2))
    print(omim)
    with open(r'c:\users\chealia\omim_ghr_2.xls','a',encoding='utf-8') as f:
        f.write('%s\t%s\t%s\n'%(l2,name,omim))
    