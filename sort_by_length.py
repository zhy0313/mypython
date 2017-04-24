# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:36:51 2017

@author: AB053658
"""
from random import random 

filename='E:\pythonworkspace\pythonlearn\mypython\words.txt'
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
输入:list:words
输出:按照word的长度从长到短排序。相同长度的按照字母顺序。
'''        
def sort_by_length(words):
    temp=[]
    for word in words:
        temp.append([len(word),word])
    temp.sort(reverse=True)
    res=[]
    for lenth,word in temp:
        res.append(word)
    return res

'''
输入:list:words
输出:按照word的长度从长到短排序。相同长度的随机排序。
'''
def unstable_sort(words):
    temp=[]
    for word in words:
        intrand=int(100*random())
        temp.append([len(word),intrand,word])
        temp.sort(reverse=True)
    res=[]
    for lenth,_,word in temp:
        res.append(word)
    return res
    pass
addlist(filename,wordslist)
testlist=['wang','chun','yang','zhang','xiang']
#print(sort_by_length(wordslist))
print(unstable_sort(wordslist))