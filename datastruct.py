# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:41:24 2017

@author: AB053658
"""
import string 

#for char in string.punctuation:
#    print(char)
#puct="    ABCDS!#$%&'()*+aaa,    -.vvv/:  ;<=>?  @[\]^_`{|}~      "
#print(puct)
#puct=puct.strip()
#print(puct)
#for char in puct:
#    if (char in string.punctuation or char in string.whitespace):
#        puct=puct.replace(char,'')
#        
#
#puct=puct.lower()
print("aafwang")
intab=string.punctuation+string.whitespace
print(intab)
outtab=' '*len(intab)
tanstab=str.maketrans(intab,outtab)
test2="    asaddsfsABCDS!#$%&'()*+aaa,   dsdasdsf   -.vvv/:  ;<=>?  @[\]^_`{|}~      "
print(test2)
test2=test2.strip()
print(test2)
test2=test2.translate(tanstab)
print(test2)
test2=test2.replace(' ','')

print(test2)
'''
输入：一行英文字母
输出：去除特殊符号，空格，大写变成小写
'''
def line_trans(words):
    intab=string.punctuation+string.whitespace
    outtab=' '*len(intab)
    transtab=str.maketrans(intab,outtab)
    #去掉空格
    words=words.strip()
    words=words.translate(transtab)
    words=words.replace(' ','')
    words=words.lower()
    return words

print(line_trans("    asaddsfsABCDS!#$%&'()*+aaa,   dsdasdsf   -.vvv/:  ;<=>?  @[\]^_`{|}~      "))