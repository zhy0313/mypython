# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:44:39 2017

@author: wangyanwu
"""

import os
'''
输入：dirname
输出：列出所有文件的名字
'''
def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
    
    
walk("E:\pythonworkspace")