# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:56:24 2018

@author: chealia
"""

import math
def P_value(a,b,c,d):
    fa=math.factorial(a)
    fb=math.factorial(b)
    fc=math.factorial(c)
    fd=math.factorial(d)
    fab=math.factorial(a+b)
    fac=math.factorial(a+c)
    fcd=math.factorial(c+d)
    fbd=math.factorial(b+d)
    fabcd=math.factorial(a+b+c+d)
    return fab*fac*fcd*fbd/(fabcd*fa*fb*fc*fd)