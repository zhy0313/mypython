# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:36:42 2017

@author: wangyanwu
"""

'''
nested_sum
输入：带有嵌套的数组。
输出：求和
'''
def nested_sum(t):
    total=0
    for i in range(len(t)):
       if isinstance(t[i],int):
           total+=t[i]
       else:
           total+=nested_sum(t[i])
    return total

t=[1,2,3,[1,2,4],[25,[1,2],34],[]]
a=[1,2,3]
print(nested_sum(t))