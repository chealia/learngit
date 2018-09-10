# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 18:52:30 2018

@author: chealia
"""

import requests
from lxml import etree
import xlrd
import re
book=xlrd.open_workbook('GHR_quchong.xls')
links2=[]#这是存下所有链接，以便后面去重
sh=book.sheet_by_index(0)
for i in range(sh.nrows):
    x=re.match('^(https://ghr.nlm.nih.gov)(.*)$',sh.cell_value(i,1)).group(2)#用正则表达式分组匹配url最后面那一截。
    links2.append(x)
print(links2)
url='https://ghr.nlm.nih.gov/condition?initial=0'#这是0~9的url,还有a的url没爬
data=requests.get(url).text
s=etree.HTML(data)
links=s.xpath('//*[@id="skip"]/div/div/div/section/ul/li/a/@href')
#links2=reduce(lambda x,y:x if y in x else x+[y],[[],]+links)#一页内的内容去重
links3=[]#存下当前页面的所有已整体去重的链接
for l1 in links:
    if l1 not in links2:#如果该链接不在整体链接库中
        links2.append(l1)#那么加入到整体链接库中
        links3.append(l1)#且增加到当前页面的链接库中
                    
for l3 in links3:
    print(l3)
    link='https://ghr.nlm.nih.gov%s'%(l3)
    print(link)
    data2=requests.get(link).text
    s2=etree.HTML(data2)
    tit=s2.xpath('//*[@id="skip"]/div/div[1]/div/section/div[1]/h1/text()')[0]
    des=s2.xpath('//*[@id="definition"]/div/div/div/div[1]/div//text()')
    desc=''.join(des)
    fre=s2.xpath('//*[@id="statistics"]/div/div/div/div[1]/div//text()')
    freq=''.join(fre)
    gen=s2.xpath('//*[@id="genes"]/div/div/div/div[1]/div[1]//text()')
    gene=''.join(gen)
    inh=s2.xpath('//*[@id="inheritance"]/div/div/div/div[1]/div//text()')
    inhe=''.join(inh)
    syn=s2.xpath('//*[@id="synonyms"]/div/div/div/div[1]/ul//text()')
    syno='; '.join(syn)
    with open('c:\\users\chealia\GHR1.xls','a',encoding='utf-8') as f:
        f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(tit,link,desc,freq,gene,inhe,syno))
        #f.write('\ntitle: %s\nlink: %s\ndescription: %s\nfrequency: %s\ngenetic_change: %sninheritance_pattern: %s\nsynonymous: %s'%(tit,link,desc,freq,gene,inhe,syno))
    