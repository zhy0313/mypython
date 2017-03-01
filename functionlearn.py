# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:10:04 2017

@author: wangyanwu
"""
from swampy.TurtleWorld import *
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

world=TurtleWorld()
bob=Turtle()
#print(bob)
#fd(bob,100)
#lt(bob)
#fd(bob,100)
#lt(bob)
#fd(bob,100)
#lt(bob)
#fd(bob,100)
#for j in range(5):
#    for i in range(4):
#        fd(bob,100-10*j)
#        lt(bob)

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)
#square(bob,150)
rt(bob)
bob.delay=0.001
#polygon(bob,180)
def circle(t,r):
    length=(2*r*math.pi)/360
    polygon(t,length,360)

circle(bob,100)
wait_for_user()