# -*- coding: utf-8 -*-
"""
Created on Wed May 03 21:19:18 2017

@author: wangyanwu
"""

import string
import re
'''
输入:filename
输出：包含单词和单词出现次数的字典hist
'''
def process_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    hist.pop('',-1)
    return hist

def myprocess_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        myprocess_line(line,hist)
    hist.pop('',-1)
    return hist
'''
输入：string，和hist字典
输出：把string 分割成一个个word，添加进hist，value为出现次数
'''
def process_line(line,hist):
    line=line.replace('-',' ')
    
    for word in line.split():
        word=word.strip(string.punctuation+string.whitespace)
        word=word.lower()
        word=' '.join(word.split())
        hist[word]=hist.get(word,0)+1

def myprocess_line(line,hist):
    line=line.replace('-',' ')
    
    for word in line.split():
        word=re.sub(r'[^A-Za-z0-9]',' ',word)
        word=word.lower()
        word=' '.join(word.split())
        hist[word]=hist.get(word,0)+1

'''
输入：dict
输出：包含的单词数
'''        
def  total_words(hist):
    return sum(hist.values())
'''
输入：dict
输出：包含单词的种数
'''
def different_words(hist):
    return len(hist)
'''
输入：dict，key 单词，value,出现次数
输出：list。按word 出现次数从高到低排序。
'''
def most_common(hist):
    temp=[]
    for key,value in hist.items():
        temp.append([value,key])
        temp.sort(reverse=True)
    res=[]
    for value,key in temp:
        res.append([key,value])
    return res
    
hist=process_file('emma.txt')
hist1=myprocess_file('emma.txt')
dictwords=myprocess_file('words.txt')
'''
输入：dict d1,d2
输出：dict .在d1中有，在d2中没有的单词。
'''
def subtract(d1,d2):
    subdict=dict()
    for key in d1:
        if key not in d2:
            subdict[key]=None
    return subdict

def mysubtract(d1,d2):
    return set(d1)-set(d2)
#print(hist)
#for i in range(10):
#    print("  ")
#print(hist1)
print(total_words(hist))
print(different_words(hist))
print(total_words(hist1))
print(different_words(hist1))

t=most_common(hist1)

print(hist.get('',-1))
for word,freq in t[:10]:
    print(word+'\t'+str(freq))
#print(hist1)   
print(mysubtract(hist1,dictwords))
