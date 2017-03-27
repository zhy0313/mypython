# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:20:21 2017

@author: wangyanwu
"""

'''
cumulative_sum
输入：一个数字组成的list
输出：一个和原来一样大小的list，list[i]=sum(list[0,i+1])

'''
def cumulative_sum(t):
    res=[]
    for i in range(len(t)):
        res.append(sum(t[:i+1]))
    return res

t=[1,2,3,5,7,8]
print(cumulative_sum(t))