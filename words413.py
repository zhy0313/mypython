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
