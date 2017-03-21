# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:06:49 2017

@author: AB053658
"""

import os

catchdir='C:\\Users\\ab053658\\AppData\Local\\Microsoft\\Windows\\INetCache'

def delCatch(catchdir):
    for files in os.listdir(catchdir):
        try:
            print("remove    "+files)
            os.remove(files)
        except Exception as e:
            continue
        

if __name__=="__main__":
    delCatch(catchdir)