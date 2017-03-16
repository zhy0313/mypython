# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 08:55:28 2017

@author: AB053658
"""

import urllib.request

url='http://www.baidu.com'


data=urllib.request.urlopen(url).read()#
data=data.decode('utf-8')
print(data)
#print("helloworld")
#f = urllib.request.urlopen('http://www.python.org/')
#print(f.read(100).decode('utf-8'))

