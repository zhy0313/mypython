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
transtab=string.maketrans(intab,outtab)

words='    wangyanwu  Zhangchunxiang Sunquan */:;<=>?@[\]^_`{|}~ wangwu lihenan     '
words=words.strip()
words=words.translate(transtab)
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
    words=words.strip(string.punctuation+string.whitespace)
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
    return worddict

def main():
    filepath="E:\pythonworkspace\pythonlearn\mypython\mybook.txt"
    print(adddict(filepath))
    
main()