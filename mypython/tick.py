# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:15:48 2017

@author: AB053658
"""

import tushare as ts
import pandas as pd
df=ts.get_tick_data('000002',date='2017-02-06')
df.tail(10)
df['time']='2017-02-06 '+df['time']
df['time']=pd.to_datetime(df['time'])
df=df.set_index('time')
df.tail(10)

price_df=df['price'].resample('1min').ohlc()

price_df=price_df.dropna()#删除空值
price_df.head(10)