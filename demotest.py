# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:26:31 2017

@author: AB053658
"""
import requests
from bs4 import BeautifulSoup

url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
#input:url
#output:respond.text
def getDemo(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
    except:
        return "产生异常"
    return r.text

demo=getDemo(url)

soap=BeautifulSoup(demo,'html.parser')
#print(soap.tbody)
#print( soap.tbody.tr.contents[6].string)
for child in soap.tbody.tr:
    
    print(child.string)
#
#for child in soap.body.descendants:
#    print(child)
#
#print(soap.title.parent)
#
#print(soap.html.parent)
#print(soap.parent)
#
#tag=soap.a
#print(tag)

#for sibling in soap.a.next_sibling:
#    print(sibling)
#
#for sibling in soap.a.previous_sibling:
#    print(sibling)