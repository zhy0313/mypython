# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:06:10 2017

@author: AB053658
"""

#from  multiprocessing import Process
from  multiprocessing import Pool
import os,time,random

#==============================================================================
# #子进程要执行的代码
#==============================================================================

def run_proc(name):
    print('Run child process %s(%s)...'%(name,os.getpid()))
    
def long_time_task(name):
    print('Run task %s(%s) ..' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.Random()*3)
    end=time.time()
    print('Task %s run %0.2f seconds.' %(name,(end-start)))
    
if __name__=='__main__':
#    print('Parent process %s.'% os.getpid())
#    p=Process(target=run_proc,args=('test',))
#    
#    print('Child process will start.')
#    
#    p.start()
#    p.join()
#    print('Child PROCESs end.')
    
    print('Parent process %s.'% os.getpid())
    k=Pool(4)
    for i in range(5):
        k.apply_async(long_time_task,args=(i,))
        
    print('Waiting for all subprocesses done ..')
    k.close()
    k.join()
    print('ALL subprocesses done')
    
    