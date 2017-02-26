# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:11:36 2017

@author: AB053658
"""

import os

try:
    home=os.path.expanduser('~')
    print(home)
    
    if not os.path.exists(home+'/testdir'):
        os.mkdir(home+'/testdir')
        
except Exception as e:
    print(e)
    
    