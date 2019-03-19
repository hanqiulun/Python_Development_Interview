# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: binary_search.py
Description : 
Project: Python_Basic_Algorithm
Last Modified: Tuesday, 19th March 2019 6:07:37 pm
-------------------------------------------------------------
'''

import time
from typing import List


def normal_search(lst: List[int], value: int) -> None or int:
    for i in lst:
        if i == value:
            return i
    return None


def binary_search_loop(lst: List[int], value: int) -> None or int:
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid
    return None


start1 = time.time()
value1 = binary_search_loop(
    lst=list(range(10000000)),
    value=9992139
)
end1 = time.time()
start2 = time.time()
value2 = normal_search(
    lst=list(range(10000000)),
    value=9992139
)
end2 = time.time()
print(f"time_cost1: {end1-start1} get_value: {value1}")
print(f"time_cost2: {end2-start2} get_value: {value2}")

# OutPut
time_cost1: 0.32248711585998535 get_value: 9992139
time_cost2: 0.5321547985076904 get_value: 9992139
