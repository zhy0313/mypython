# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:47:45 2017

@author: AB053658
"""
import tushare as ts

df=ts.realtime_boxoffice()
print(df)
ds=ts.day_boxoffice()
print(ds)


dv=ts.shibor_data(2013)
print(dv.sort_values('ON',ascending=False).head(10))
du = ts.get_realtime_quotes('000581') #Single stock symbol
du[['code','name','price','bid','ask','volume','amount','time']]
print(du)

dw=ts.get_index()
print(dw)
