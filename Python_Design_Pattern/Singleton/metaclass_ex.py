# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: metaclass_ex.py
Description : 
Project: Singleton
Last Modified: Monday, 25th March 2019 12:18:52 am
-------------------------------------------------------------
'''

class SingletonType(type):
    def __init__(self,*args,**kwargs):
        super(SingletonType,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs): # 这里的cls，即Foo类
        print('cls',cls)
        obj = cls.__new__(cls,*args, **kwargs)
        cls.__init__(obj,*args, **kwargs) # Foo.__init__(obj)
        return obj

class Foo(metaclass=SingletonType): # 指定创建Foo的type为SingletonType
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

obj = Foo('xx')