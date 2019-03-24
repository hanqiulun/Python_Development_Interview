# -*- coding: utf-8 -*-

from typing import Any
'''
------------------------------------------------------------
File Name: climb_stairs.py
Description : 
Project: Python_Algorithm_Example
Last Modified: Monday, 25th March 2019 1:08:10 am
-------------------------------------------------------------
'''

"""

a staircase has n steps， You can only climb the first or second order at a time, and ask you how to climb the stairs.
"""

"""
一个楼梯有n阶，你每次只能登上一阶或是两阶，问你有几种方法登上楼梯
"""


# 1 recursion


def recursionClimbStairs(n: int) -> Any:
    if n <= 2:
        return 2
    return recursionClimbStairs(n-1) + recursionClimbStairs(n-2)


# print(recursionClimbStairs(100)) error Recursion times excessive


# 2 iteration


def climbStairs(n: int) -> int:
    nums = [1, 2]
    if n <= 2:
        return n
    for i in range(2, n):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[len(nums) - 1]


print(climbStairs(100)) correct
