# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: singleton_by_class.py
Description : 
Project: Singleton
Last Modified: Monday, 25th March 2019 12:00:47 am
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


a1 = Singleton.instance()
a2 = Singleton.instance()

print(f"a1 id: {id(a1)}")
print(f"a2 id: {id(a2)}")