# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:26:31 2017

@author: AB053658
"""
import requests
import bs4
#import numpy as np
 
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


ulist=[]
def fillUnivList(demo,ulist):
    soap=bs4.BeautifulSoup(demo,'html.parser')
    #print(soap.tbody)
    #print( soap.tbody.tr.contents[6].string)
    for tr in soap.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            
            tds=tr('td')
#            print(tds[1].string)
            ulist.append([tds[1].string,tds[2].string,tds[3].string])
            
def PrintInfo(info,num):
    tplit="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplit.format("排名","学校","总分",chr(12288)))
    for i in range(num):
        u=info[i]
        print(tplit.format(u[0],u[1],u[2],chr(12288)))


if __name__=="__main__":
    demo=getDemo(url)
    fillUnivList(demo,ulist)
#    print(len(ulist))
    PrintInfo(ulist,20)
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