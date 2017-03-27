# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:04:34 2017

@author: wangyanwu
"""

'''
nested_capitalized
输入：nested string list
输出： 大写的内建的string list
'''
def nested_capitalized(t):
    res=[]
    for s in t:
        if(isinstance(s,str)):
            res.append(s.capitalize())
        else:
            
            res.append(nested_capitalized(s))
    return res

t=['wangyanyu','lihenan',['sunquan',['aaffds','ccdd'],'wangyu']]

print(nested_capitalized(t))
