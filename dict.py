# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:10:11 2017

@author: AB053658
"""

eng2sp=dict()
eng2sp['wangyanwu']='zhangchunxiang'
eng2sp['sunquan']='zhujiahong'
eng2sp['lihenan']='wangcunli'
print(eng2sp['sunquan'])
print('sunquan' in eng2sp)

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
       
addwords(wordslist,filepath)
adddict(eng2sp,filepath)
print(eng2sp['zymurgies'])
#print(eng2sp)