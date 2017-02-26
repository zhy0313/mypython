# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:38:17 2017

@author: AB053658
"""
import os,re,sys
import re

cf = open(os.path.dirname(__file__)+"/settings.conf",'r')


db_info = re.findall('db_info=.*',cf.read())[0].replace('db_info=','')

print(db_info)
