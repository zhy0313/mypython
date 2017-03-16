# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:33:52 2017

@author: AB053658
"""
import urllib.request

import re
from os.path import basename
import os
#图片存储目录
downdir='D:\\pythonworkspace\\mypython\\downloads'

url = "http://tieba.baidu.com/p/2166231880"
def getPage(url):
    url=url+"?see_lz=1"
#    print(url)
    urlContent = urllib.request.urlopen(url).read()
    page=b'<span class="red">(.*?)</span>'
#    page="b'百度贴吧'"
#    print(urlContent)
    thePage=re.findall(page,urlContent)
#    print(thePage[0])
    return int(thePage[0])
    
#print("baidutieba")
def downImg(url):
#更改目录
	os.chdir(downdir)
	urlContent = urllib.request.urlopen(url).read()	
	spans=b'<cc>(.*?)</cc>'
	ss=re.findall(spans,urlContent)
#查找所有的url
	obImgs=b','.join(ss)
	imgUrls = re.findall(b'img .*?src="(.*?\.jpg)"', obImgs)
	print((str(imgUrls[0]).replace('^b','')))
	for imgUrl in imgUrls:
		try:
		    print("wangyan")
		    imgUrl1=re.findall('\'(.*?)\'',str(imgUrl))[0]
		    print(imgUrl1)                
#		    imgData = urllib.request.urlopen(imgUrl1).read()
		    print("aa")      
		    fileName = basename(urllib.parse.urlsplit(imgUrl)[2])
#		    print(urllib.parse.urlsplit(imgUrl)[2])                
#		    output = open(fileName,'wb')
#		    output.write(imgData)
#		    output.close()
		    urllib.request.urlretrieve(imgUrl1,fileName)
		except:
		    print ("Er..")
url1="http://tieba.baidu.com/p/2166231880?see_lz=1&pn=1"
downImg(url1)
