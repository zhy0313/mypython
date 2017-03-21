# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:47:48 2017

@author: AB053658
"""
import math
def  printN(n):
    while n!=1:
        print (n)
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

def donePrint():
    while(True):
        line=input('>')
        print(line)
        if(line=="done"):
            
            break
    print("Done")
'''输入：a
输出：a的平方根。
方法：牛顿法
y=(x+a/x)/2
'''    
def square_root(a):
    x=int(a/3)
    epsilon=0.000000000001
    while(True):
#        print(x)
        y=(x+a/x)/2
        if(abs(y-x)<epsilon):
            break
        x=y
    return x

'''
输入：string
输出：string反向输出
'''
def reverseString(string):
    length=len(string)
    while(length>0):
#        print(str(length)+"test1")
        print(string[length-1],end='')
        length=length-1
#        print(str(length)+"test")


#print(square_root(225))
#print(math.exp(0))

reverseString("lihenan")

'''
输出：自动生成名字。
'''
def printName():
    prefixes='JKLMNOPQ'
    suffix='ack'
    
    for letter in prefixes:
        print(letter+suffix)
    prefixes1='OQ'
    suffix1='uack'
    for letter in prefixes1:
        print(letter+suffix1)
   
'''
输入：string,字母：a
输出：count。字母在string中出现的次数 
'''     
def count(string,a):
    count=0
    for i in range(len(string)):
        if(string[i]==a):
            count=count+1
    return count
'''
输入：string,字母：a
输出：count。字母在string中出现的次数 
使用第三方函数 find
'''       
def countv1(string,a):
    pass       
printName()

print(count("dsddsfldsflfddsffsdffds",'d'))