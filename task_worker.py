# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:11:22 2018

@author: chealia
"""
import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server_addr='12.0.0.1'
print('Try to connect to server %s...'%server_addr)
m=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()
for i in range(10):
    try:
        n=task.get(timeout=10)
        print('we get %s'%n)
        print('now we calculte %s*%s'%(n,n))
        r='%d*%d=%d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task_queue is empty, all work have done')
print('worker quit')





































