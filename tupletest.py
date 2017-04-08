# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:40:19 2017

@author: AB053658
"""
'''
输入：2个数字
输出：他们除数和余数。以tuple 输出。
'''
def mydivmod(a,b):
    if isinstance(a,str) or isinstance(b,str):
        print(str(a)+'or'+str(b)+"can't be str") 
        return
    elif(b!=0):
        return int(a/b),a%b
    else:
        print(str(b)+"can't be 0!")
        return 

'''
输入：tuple.
输出：他们的和。sum
'''   
def sum_all(*args):  
    result=0
    for i in args:
        result+=i
    return result
        
    pass

print (mydivmod(10,4))
print(divmod(10,4))
print(sum_all(1,2,3,4,10))
print(dict(zip('abc',range(3))))
mydict=dict()
mydict.update({"wangyanwu":"zhangchunxiang"})
print(mydict.get('wangyanwu'))