# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:16:04 2017

@author: AB053658
"""

import requests
import re 
from bs4 import BeautifulSoup
import traceback

'''
输入：网页url
输出：网页，text
'''
def getHTMLText(url,encoding='utf-8'):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=encoding
        return r.text
    except:
        return "产生异常"


'''
输入：html
输出：stocklist
'''
def getStockList(html,stocklist):
    soup=BeautifulSoup(html,"html.parser")
    for link in soup.find_all('a'):
#        print(link.get('href'))
        
        ls=re.search(r's[hz](6|3|0)\d{5}',str(link.get('href')))
        if(ls):
#            print(ls.group(0))
            stocklist.append(ls.group(0))
        else:
            continue
       
    pass
'''
输入：个股url，stocklist，filepath
输出：打印文件
'''
def getStockinfo(stocklist,stockurl,filepath):
    for i in stocklist:
        stockinfo_url=stockurl+str(i)+'.html'
        print(stockinfo_url)
        try:
            html=getHTMLText(stockinfo_url)
            if (html==''):
                continue
            infodict=dict()
            soup=BeautifulSoup(html,'html.parser')
            stockinfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockinfo.find_all('a',attrs={'class':'bets-name'})[0]
            print(name.text.split()[0])
            infodict.update({'股票名称': name.text.split()[0],"股票代码":i})
            keylist=stockinfo.find_all('dt')
            valuelist=stockinfo.find_all('dd')
            for j in range(len(keylist)):
                infodict[keylist[j].text]=valuelist[j].text
            print(infodict)
            with open(filepath,'a',encoding='utf-8') as f:
                f.write(str(infodict)+'\n')
        except:
            continue
        

#    pass
def main():
   stocklist_url='http://quote.eastmoney.com/stocklist.html'
   stockinfo_url='https://gupiao.baidu.com/stock/'
   stocklist=[]
   filepath="D:\pythonworkspace\mypython\BaiduStockInfo.txt"
   html=getHTMLText(stocklist_url)
   getStockList(html,stocklist)
   getStockinfo(stocklist,stockinfo_url,filepath)

main()