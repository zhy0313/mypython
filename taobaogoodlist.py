# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:03:13 2017

@author: wangyanwu
"""
import requests
import re

#输入：url
#输出：html
def GetHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ("产生异常")
    

#输入：html
#输出：数组ilt
def parsePage(ilt,html):
    try:
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([title,price])
    except:
        print " "
       
#输入：数组ilt
#输出：商品列表
def PrintGoodList(ilt):
    tplt="{0:^4}\t{1:^16}\t{2:^8}"
    print(tplt.format("序号","标题","价格"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    

def main():
    depth=3
    good="飞机杯男用"
    urlstart="https://s.taobao.com/search?q="+good
    infolist=[]
    for i in range(depth):
                try:
                    url=urlstart+"&s="+str(44*i)
                    html=GetHTMLText(url)
                    parsePage(infolist,html)
                except:
                    continue
    PrintGoodList(infolist)

main()
        

    


