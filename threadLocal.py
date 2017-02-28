# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:09:05 2017

@author: wangyanwu
"""

import threading

local_school=threading.local()

def process_student():
    print('hello,%s (in %s)'%(local_school.student,threading.current_thread().name))

def process_thread(name):
    local_school.student=name
    process_student()


t1=threading.Thread(target=process_thread,args=('wangyanwu',),name='Thread A')
t2=threading.Thread(target=process_thread,args=('lihenan',),name='Thread B')

t1.start()
t2.start()
t1.join()
t2.join()
