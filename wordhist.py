# -*- coding: utf-8 -*-
"""
Created on Wed May 03 21:19:18 2017

@author: wangyanwu
"""

import string

def process_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line=line.replace('-',' ')
    
    for word in line.split():
        word=word.strip(string.punctuation+string.whitespace)
        word=word.lower()
        
        hist[word]=hist.get(word,0)+1

hist=process_file('emma.txt')

print(hist)