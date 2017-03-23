# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:32:33 2017

@author: wangyanwu
"""

from swampy.TurtleWorld import *
'''
输入：bob对象
输出：三角形
'''

def draw_angle(bob):
    fd(bob,30)
    lt(bob)
    fd(bob,40)
    lt(bob,135)
    fd(bob,50)
    
    
world=TurtleWorld()
bob=Turtle()
print bob

draw_angle(bob)
wait_for_user()

