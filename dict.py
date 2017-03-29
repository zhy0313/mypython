# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:10:11 2017

@author: AB053658
"""
import time 
eng2sp=dict()
eng2sp['wangyanwu']='zhangchunxiang'
eng2sp['sunquan']='zhujiahong'
eng2sp['lihenan']='wangcunli'
print(eng2sp['sunquan'])
print('sunquan' in eng2sp)
eng2sp.update({"股票代码" : "000002","股票名称":"万科A"})
print(eng2sp)
wordslist=[]
filepath="D://pythonworkspace//mypython//words.txt"
'''
输入：wordslist,filename
输出：将filename里面的单词读进wordslist
'''
def addwords(wordslist,filename):
    fin=open(filename)
    for line in fin:
        word=line.strip()
#        print(word)
        wordslist.append(word)
'''
输入：dictname,filename
输出：将filename里面的单词读进dictname作为key，value为读入时的计数。
'''
def adddict(dictname,filename):
    fin=open(filename)
    count=0
    for line in fin:
       word=line.strip()
       dictname[word]=count
       count+=1
  
'''
输入：字符串word，数组wordslist
输出：如果在wordslist中找到word，返回下标，否则返回-1
'''     
def listfind(word,wordslist):
    for i in range(len(wordslist)):
        if(word==wordslist[i]):
            return i
    return -1
       
addwords(wordslist,filepath)
adddict(eng2sp,filepath)
t1=time.time()
#print(eng2sp['zymurgies'])
for i in range(100):
    listfind('zymurgies',wordslist)
t2=time.time()
print(t2-t1)

t3=time.time()
for i in range(10000):
#    eng2sp['zymurgies']
    'zymurgies' in eng2sp
t4=time.time()
print(t4-t3)


#print(eng2sp)