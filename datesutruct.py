# -*- coding: utf-8 -*-
"""
Created on Wed May 03 20:12:48 2017

@author: wangyanwu
"""


def histtogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
t=['a','a','b']
hist=histtogram(t)
print(hist)
