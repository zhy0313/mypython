# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:21:14 2017

@author: wangyanwu
"""
import os
camels=42
print('I have spotted %d camels.'%camels)
print('In %d years I have spotted %g %s.'%(3,0.1,'camels'))

cwd=os.getcwd()
print(cwd)
print(os.path.abspath("words.txt"))
print(os.listdir(cwd))