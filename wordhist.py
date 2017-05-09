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
    return hist

def myprocess_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        myprocess_line(line,hist)
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
        
        hist[word]=hist.get(word,0)+1

def myprocess_line(line,hist):
    line=line.replace('-',' ')
    
    for word in line.split():
        word=re.sub(r'[^A-Za-z0-9]',' ',word)
        word=word.lower()
        
        hist[word]=hist.get(word,0)+1
        
def  total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

hist=process_file('emma.txt')
hist1=myprocess_file('emma.txt')



#print(hist)
for i in range(10):
    print("  ")
print(hist1)
print(total_words(hist))
print(different_words(hist))
print(total_words(hist1))
print(different_words(hist1))