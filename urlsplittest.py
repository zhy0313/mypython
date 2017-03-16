# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:27:06 2017

@author: AB053658
"""
import urllib
import os
from os.path import basename

url='http://img109.icxo.com/200611/200611851401.jpg'
downdir='D:\\pythonworkspace\\mypython\\downloads'
print(url)
urlsplit=urllib.parse.urlsplit(url)

print(urlsplit[2])
filename=basename(urlsplit[2])
imgData = urllib.request.urlopen(url).read()
print(filename)
os.chdir(downdir)
output=open(filename,'wb')
output.write(imgData)
output.close()

