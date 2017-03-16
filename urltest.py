# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:00:32 2017

@author: AB053658
"""

import urllib
import os
from os.path import basename
import re
#图片存储目录
downdir='D:\\pythonworkspace\\mypython\\downloads'
url='http://tieba.baidu.com/p/2166231880'

def get_html(url):  
    page = urllib.request.urlopen(url)  
    html = page.read().decode('utf-8')  
    return html  
  
def get_img(html):
    os.chdir(downdir)
    reg = r'src="(.*?\.jpg)" bdwater='  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre, html)  
 
    for imgurl in imglist: 
        print(imgurl)
#        imgurl=re.findall('\'(.*?)\'',str(imgurl))[0]
        fileName = basename(urllib.parse.urlsplit(imgurl)[2])
        urllib.request.urlretrieve(imgurl, fileName)  
          
html = get_html(url)  
print (get_img(html))  