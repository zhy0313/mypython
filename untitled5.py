# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:48:51 2017

@author: AB053658
"""
import PyFetion 

#import os

print("pyfetion")
def SendSMS(sms):
    myphone = '18810543929'
    mypwd = 'wangyanwu2015'
    tophone = '15010212095'

    fetion = PyFetion(myphone,mypwd,'TCP')
    fetion.login(FetionHidden)
    print ('send to '+tophone)
    fetion.send_sms(sms,tophone,True)
    print ('OK')

    fetion.logout()
    return True

msg = "hello world"
SendSMS(msg)
print ('OK!!!')
