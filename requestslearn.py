# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:39:15 2017

@author: AB053658
"""

import requests

#r=requests.get("http://www.baidu.com")
#
#print(r.status_code)
#print(r.encoding)
#print(r.apparent_encoding)
#print(type(r))
#r.encoding='utf-8'
#print(r.text)

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__=="__main__":
    print(getHTMLText("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"))