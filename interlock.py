# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:09:27 2017

@author: AB053658
"""

'''
interlock
输出word.txt里面的interlock 单词。
即一个单词是由另2个单词的字母按顺序交替组合产生。比如shoe 和cold交替产生schooled
'''
from time import time

filename='D:\pythonworkspace\mypython\words.txt'
wordslist=[]
'''
输入：list：wordlist,file:filename
输出：把word.txt里面的单词添加到wordlist
'''
def addlist(filepath,wordslist):
    fin=open(filename)
    for line in fin:
        word=line.strip()
        wordslist.append(word)
'''
输入：list:wordslist
输出：interlock，word1，word2
'''
def interlock(wordslist):
    for word in wordslist:
        if(len(word)<4):
            continue
        else:
            first=word[::2]
            second=word[1::2]
            if((besect(wordslist,first)!=-1) and(besect(wordslist,second)!=-1)):
                print(word,first,second)

def interlock1(wordslist):
    for word in wordslist:
            first=word[::2]
            second=word[1::2]
            if((besect(wordslist,first)!=-1) and(besect(wordslist,second)!=-1)):
                print(word,first,second)
                
def interlock(wordslist,n=2):
    for word in wordslist:
        test=['']*n
        for i in range(n):
            test[i]=word[i::n]
            flag=True
            for i in test:
                 if(besect(wordslist,i)==-1):
                     flag=False
                     break
            if(flag):
                print(word,test)
'''
输入：list:wordslist(按字母顺序排序的),string:word
输出：i。如果word在wordslist，返回下标i,否则返回-1
运用二分法查找。
循环法：
while(low<high)
low=0,high=len(list)-1;mid=(high-low)/2+low(防止low+high超过int的最大值，导致溢出)
1、如果list[mid]=word,返回mid
    2、如果list[mid]<word,low=mid+1;
    递归查询
    3、如果list[mid]>word,high=mid-1;
   如果都没有。返回-1
'''
def besect(wordslist,word):
    low=0
    high=len(wordslist)-1
    while(low<high):
        mid=int((high-low)/2+low)
        if(wordslist[mid]==word):
            return mid
        elif (wordslist[mid]<word):
            low=mid+1
        else:
            high=mid-1
    
    return -1

          
    
    
addlist(filename,wordslist)


#print(besect(wordslist,'zymology'))
t1=time()
interlock(wordslist)
t2=time()
print(t2-t1)
t3=time()
interlock1(wordslist)
t4=time()
print(t4-t3)
interlock(wordslist,n=5)