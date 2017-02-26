# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:55:39 2017

@author: AB053658
"""

import tushare as ts

ts.set_broker('gdzq',user='30221610',passwd='860413')
df=ts.get_broker()
print(df)
csc=ts.TraderAPI('gdzq')

csc.login()
baseinfo=csc.baseinfo()
print(baseinfo)

