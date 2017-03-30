# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:48:29 2017

@author: AB053658
"""

def binary_search(num,array,left_index=0):
    binary_index = int(len(array)/2)
#    print(len(array),binary_index,array[binary_index],left_index)
    
    if num < array[binary_index]:
        
        binary_search(num,array[0:binary_index],left_index)
    elif num > array[binary_index]:
        left_index = left_index + binary_index
        binary_search(num,array[binary_index:len(array)],left_index)
    else:
        print (left_index+binary_index)
 
if __name__ == '__main__':
    array = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
    binary_search(13,array)
    print(array[11])