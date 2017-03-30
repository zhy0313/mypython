# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:18:53 2017

@author: wangyanwu
"""

fin=open('words.txt')

'''
输入：word
输出：包含e，返回False，不含e，返回True
'''
def has_no_e(word):
    result=word.find('e')
    if(result==-1):
        return True
    else:
        return False
    
print (fin)

total=0
e_count=0
temp=fin.readline()
while(temp!=''):
    temp=temp.strip()
    if(has_no_e(temp)):
        e_count=e_count+1
    total=total+1
    temp=fin.readline()

print (total,' ',e_count)
result=float(e_count)/total
print (result)
tplt="{0:2,.2f}"
print(tplt.format(float(e_count)/total*100)+'%')