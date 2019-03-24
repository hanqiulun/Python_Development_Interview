# -*- coding: utf-8 -*-


'''
------------------------------------------------------------
File Name: singleton_by_class_mutli_threading_sleep.py
Description : 
Project: Singleton
Last Modified: Monday, 25th March 2019 12:04:58 am
-------------------------------------------------------------
'''


class Singleton:

    def __init__(self):
        import time
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

import threading

def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()