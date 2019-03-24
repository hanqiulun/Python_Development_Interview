# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: singleton_by_decorator.py
Description : 
Project: Singleton
Last Modified: Sunday, 24th March 2019 11:50:08 pm
-------------------------------------------------------------
'''


def Singleton(cls):
    _instance = {}
    count = 0

    def _singleton(*args, **kargs):
        nonlocal count
        if cls not in _instance:
            print(f"count: {count}: {cls.__name__} not init")
            _instance[cls] = cls(*args, **kargs)
        else:
            print(f"count: {count}: {cls.__name__} alreay init")
        count+=1
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

print(f"a1 id: {id(a1)}, a1 value: {a1.x}")
print(f"a2 id: {id(a2)}, a2 value: {a2.x}")
