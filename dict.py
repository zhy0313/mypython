# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:10:11 2017

@author: AB053658
"""
import time 
eng2sp=dict()
eng2sp['wangyanwu']='zhangchunxiang'
eng2sp['sunquan']='zhujiahong'
eng2sp['lihenan']='wangcunli'
print(eng2sp['sunquan'])
print('sunquan' in eng2sp)
eng2sp.update({"股票代码" : "000002","股票名称":"万科A"})
print(eng2sp)
wordslist=[]
filepath="D://pythonworkspace//mypython//words.txt"
'''
输入：wordslist,filename
输出：将filename里面的单词读进wordslist
'''
def addwords(wordslist,filename):
    fin=open(filename)
    for line in fin:
        word=line.strip()
#        print(word)
        wordslist.append(word)
'''
输入：dictname,filename
输出：将filename里面的单词读进dictname作为key，value为读入时的计数。
'''
def adddict(dictname,filename):
    fin=open(filename)
    count=0
    for line in fin:
       word=line.strip()
       dictname[word]=count
       count+=1
  
'''
输入：字符串word，数组wordslist
输出：如果在wordslist中找到word，返回下标，否则返回-1
'''     
def listfind(word,wordslist):
    for i in range(len(wordslist)):
        if(word==wordslist[i]):
            return i
    return -1
       
'''
输入：一个按字母顺序排序的list，一个word
输出：返回word在list中的下标，如果没有找到返回-1
运用二分法查找。
递归法：
left=0,right=len(list);mid=(left+right)/2
1、如果list[mid]=word,返回mid
    2、如果list[mid]<word,left=mid+1;
    递归查询bisectsearch(word,wordslist[left:right])
    3、如果list[mid]>word,right=mid;
    递归查询bisectsearch(word,wordslist[left:right])
    如果len（list[left,right])=1,返回-1
'''
def bisectsearch(word,wordslist):
    left=0
    right=len(wordslist)-1
    
#    print(str(left),str(right),str(mid))
    while(right>=left):
        mid=int((right-left)/2+left)
        if(wordslist[mid]==word):
#            print("mid"+str(mid))
            return mid
        elif(wordslist[mid]<word):
            left=mid+1
#            print("left"+str(left))
#            bisectsearch(word,wordslist[left:right])
        else:
            right=mid-1
#            print("right"+str(right))
#            bisectsearch(word,wordslist[left:right])
    return -1
    
    
'''
输入：wordslist
输出：把wordslist中倒序跟原来相同的字母输出。
'''
def reverse_pair(wordslist):
    for word in wordslist:
        if(isreverse(word)):
            print(word)
    
'''
输入：word
输出：如果word的reverse和word相等，返回true，否则返回false
'''
def isreverse(word):
    return word==word[::-1]
'''
输入：wordslist
输出：word1，word2,interlock。其中interlock是有word1和word2的字母交替产生的。
'''
def interlock(wordslist):
    
    for i in range(len(wordslist)):
        wordlen=len(wordslist[i])
        j=i+1
#        print(i,j,"aa")
        
        while(j<len(wordslist)):
            if(len(wordslist[j])==wordlen):
                interlock1=mergewords(wordslist[i],wordslist[j])
                interlock2=mergewords(wordslist[j],wordslist[i])
                temp1=bisectsearch(interlock1,wordslist)
                temp2=bisectsearch(interlock2,wordslist)
#                print(i,j)
                if(temp1!=-1):
                    print(wordslist[i],wordslist[j],interlock1)
                    j=j+1
                elif(temp2!=-1):
                    print(wordslist[i],wordslist[j],interlock2)
                    j=j+1
                else:
                    j=j+1
            else:
                j=j+1

'''
输入：2个长度相同的字母。
输出：把 2个长度相同的单词交替合并
如果字母长度不等，返回null
'''
def mergewords(word1,word2):
    if(len(word1)!=len(word2)):
        return
    interlock=''
    for i in range(len(word1)):
        interlock+=word1[i]+word2[i]
        
    return interlock
    
    
addwords(wordslist,filepath)
print(bisectsearch('zymurgy',wordslist))
adddict(eng2sp,filepath)
t1=time.time()
#print(eng2sp['zymurgies'])
for i in range(100):
    listfind('zymurgies',wordslist)
t2=time.time()
print(t2-t1)

t3=time.time()
for i in range(10000):
#    eng2sp['zymurgies']
    'zymurgies' in eng2sp
t4=time.time()
print(t4-t3)

#reverse_pair(wordslist)
#print(eng2sp)

#print(mergewords('shoe','cold'))
interlock(wordslist)