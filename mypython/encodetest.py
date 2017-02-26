# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:24:08 2017

@author: AB053658
"""

import chardet
import os,sys

#编码形式
code_list=['utf-8','GB2312','gbk']

try:
    directory=sys.argv[1]
except IndexError:
    sys.exit("Must provide an argument.")

for (path,dirs,files) in os.walk(directory):
    for file in files:
        filename=os.path.join(path,file)
        with open(filename,'rb') as t:
            text=t.read()
#            print 'type(text)'
            
            code=chardet.detect(text)['encoding']
            print (filename,code)
#            if code!='utf-8':
#                new_content=text.decode(code).encode('utf-8')
#                open(filename,'wb').write(new_content)
            
            