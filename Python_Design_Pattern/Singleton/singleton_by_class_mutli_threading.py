# -*- coding: utf-8 -*-


'''
------------------------------------------------------------
File Name: singleton_by_class_mutli_threading.py
Description : 
Project: Singleton
Last Modified: Monday, 25th March 2019 12:03:12 am
-------------------------------------------------------------
'''

class Singleton:

    def __init__(self):
        pass

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