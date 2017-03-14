# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:00:57 2017

@author: wangyanwu
"""
import math
def length_hypotenuse(a,b):
    temp=a**2+b**2
#    print(temp)
    result=math.sqrt(temp)
#    print(result)
    return result
    
print(length_hypotenuse(12,5))

def is_between(x, y, z):
    if x<y and y<z:
        return True
    else:
        return False

print(is_between(5,4,4))

def fibonacci(n):
    if not isinstance(n,int):
        print 'fibonacci is only defined for integers.'
    elif n<0:
        print 'fibonacci is not defined for negative integers.'
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(20))


            