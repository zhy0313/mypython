# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:51:00 2017

@author: AB053658
"""

import pandas as pd
import numpy as np 
import tushare as ts

df=ts.forecast_data(2016,4)

df.head(20)
print(df.head(20))
df=df.set_index('code')
df=df.sort_index()
#print(df['name'])
print(df.loc['300383',['name','type']])
print(df.iloc[0:3,1:5])
zipcode='002134'
print(zipcode)
