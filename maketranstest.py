# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:36:10 2017

@author: AB053658
"""

import string   # 引用 maketrans 函数。

intab = "aeiou"
outtab = ['']*len(intab)
print(outtab)
#trantab = str.maketrans(intab, str(outtab))

str = "this is string example....wow!!!"
print (str.translate(trantab))