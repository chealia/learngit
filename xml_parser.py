# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:44:54 2018

@author: chealia
"""

import xml.etree.ElementTree as ET

if __name__=='__main__':
    filename=r'c:\users\chealia\country.xml'
    try:
        tree=ET.parse(filename)
        root=tree.getroot()
        root_lists=[]
        for child in root:
            root_list=[child.tag,child.attrib]
            root_lists.append(root_list)
            print(child.tag,child.attrib)
        print(root_lists)
        
        country=root.findall('country')
        country_lists=[]
        for s in country:
            rank=s.find('rank').text
            year=s.find('year').text
            neighbor=s.find('neighbor')
            print(rank,year,neighbor)
            country_list=[rank,year,neighbor]
            country_lists.append(country_list)
        print(country_lists)
    except Exception:
        print('open file fail')









            