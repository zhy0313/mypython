# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:12:00 2017

@author: AB053658
"""

import requests
import bs4
import os
import urllib
from os.path import basename

def getDemo(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
    except:
        return "产生异常"
    return r.text


def fillImgUrl(demo,imgList):
    soap=bs4.BeautifulSoup(demo,'html.parser')
    for link in soap.find_all('img'):
#        print(link.get("class"))
        if(link.get("class")==['BDE_Image']):
#            print(link.get("src"))
            imgList.append(link.get("src"))
    pass

def loadImg(imgList,loaddir):
    os.chdir(loaddir)
    for imgurl in imgList:
        try:
            fileName = basename(urllib.parse.urlsplit(imgurl)[2])
#            print(fileName)
            urllib.request.urlretrieve(imgurl,fileName)
        except:
            print ("Er..")
    


if __name__=="__main__":
    url="http://tieba.baidu.com/p/4828397202"
    loaddir="D:\\pythonworkspace\\mypython\\downloads"
    imgList=[]
    demo=getDemo(url)
    fillImgUrl(demo,imgList)
    loadImg(imgList,loaddir)
