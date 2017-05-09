# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:49:27 2017

@author: AB053658
"""

import random
import sys

def knuth(n,m):
    i=0
    maxint=sys.maxsize
    while(i<n):
        if(random.randint(0,maxint)%(n-i)<m):
            print(i)
            m=m-1
        i=i+1
        
knuth(100000,3)       
        
        