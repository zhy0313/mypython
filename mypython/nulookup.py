# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:17:41 2017

@author: AB053658
"""

import subprocess

print('nslookup github.com ')

r=subprocess.call(['nslookup','github.com'])
print('EXitcode:',r)