# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:23:01 2017

@author: wangyanwu
"""
'''
输入：word1,word2
输出:相等True，不等False
'''
def is_reverse(word1,word2):
    if(len(word1)!=len(word2)):
        return False
    i=0
    j=len(word2)-1
    while j>=0:
#        print i,j
        if(word1[i]!=word2[j]):
            return False
        else:
            i=i+1
            j=j-1
    
    return True
#print "wangyanwu"    
#print("is_reverse")
print(is_reverse('stop','pots'))

'''
输入：一个字符串
输出：如果是回文，返回Ture，否则False
'''
def is_palindrome(word):
    return word==word[::-1]

'''
输入：word1,word2
输出:相等True，不等False
'''
def is_reverse1(word1,word2):
    return (word1==word2[::-1])

print(is_palindrome('stop'))
print(is_reverse1('stop','pots'))    