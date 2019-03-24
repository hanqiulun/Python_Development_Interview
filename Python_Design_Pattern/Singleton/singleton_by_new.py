# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: singleton_by_new.py
Description : 
Project: Singleton
Last Modified: Monday, 25th March 2019 12:12:07 am
-------------------------------------------------------------
'''


import threading
class Singleton:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super(Singleton,cls).__new__(cls,*args, **kwargs)  
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()