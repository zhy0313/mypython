# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:52:07 2017

@author: wangyanwu
"""
import re
import string
print (string.punctuation)

print(string.whitespace)
intab=string.punctuation+string.whitespace
outtab=' '*len(intab)
#transtab=string.maketrans(intab,outtab)

words='    wangyanwu  Zhangchunxiang Sunquan */:;<=>?@[\]^_`{|}~ wangwu lihenan     '
words=words.strip()
#words=words.translate(transtab)
print('------------')
words=re.sub(r'[^A-Za-z0-9]',' ',words)
words=words.lower()
words=' '.join(words.split())
test=re.sub(' +',' ',words)
print(test)
print(words.split(' '))

'''
输入：string
输出：wordlist
'''
def splitline(words):
#   intab=string.punctuation+string.whitespace+'—'
#   outtab=' '*len(intab)
#   transtab=string.maketrans(intab,outtab) 
    words=words.replace('-',' ')
#    words=words.strip(string.punctuation+string.whitespace)
    words=re.sub(r'[^A-Za-z0-9]',' ',words)
#   words=words.translate(transtab)
    words=words.lower()
    words=' '.join(words.split())
    return words.split(' ')

'''
输入：filepath
输出：把单词读入，写道dictname里，键为单词，值为单词出现次数
'''
def adddict(filepath):
    worddict=dict()
    fin=open(filepath)
    
    for line in fin:
        wordslist=splitline(line)
#        print(wordslist)
        for word in wordslist:
            if word not in worddict:
                worddict[word]=1
            else:
                worddict[word]+=1
    worddict.pop('',0)                    
    return worddict

'''
输入：dict，n
输出：list.包含单词和频率，按频率从大到小排序。
'''
def topword(worddict):
    temp=[]
    for key,value in worddict.items():
        temp.append([value,key])
    temp.sort(reverse=True)
    res=[]
    for value,key in temp:
        res.append([key,value])
    return res
    
        
 
def main():
    filepath="E:\pythonworkspace\pythonlearn\mypython\mybook.txt"
    hist=adddict(filepath)
    t=topword(hist)
    for word,freq in t[0:20]:
        print(word+'\t'+str(freq))
main()