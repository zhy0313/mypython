# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:10:04 2017

@author: wangyanwu
"""

import math 

print(math.sqrt(2)/2)



def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    

repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)    

print_twice('spam '*4)
