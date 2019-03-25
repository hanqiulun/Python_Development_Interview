# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: 寻找两个有序数组的中位数.py
Description :
Project: LeetCode_ZH
Last Modified: Tuesday, 26th March 2019 12:03:35 am
-------------------------------------------------------------
'''
from typing import (
    List
)

nums1 = [1, 2]
nums2 = [3, 4]


def a(lst1: List[int], lst2: List[int]) -> int:
    m, n = len(lst1), len(lst2)
    if m > n:
        lst1, lst2, m, n = lst2, lst1, n, m
    if n == 0:
        raise ValueError
    imin, imax, half_len = 0, m, (m+n+1)/2
    while imin < imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and lst2[j-1] > lst1[i]:
            imin = i+1
        elif i > 0 and lst1[i-1] > lst2[j]:
            imax = j-1
        else:
            if i == 0:
                max_left = lst2[j-1]
            elif j == 0:
                max_left = lst1[i-1]
            else:
                max_left = max(lst1[i-1], lst2[j-1])
            if (m+n)/2 == 1:
                return max_left
            if i == m:
                min_right = lst2[j]
            elif j == n:
                min_right = lst1[i]
            else:
                min_right = min(lst1[i], lst2[j])
            return (min_right+max_left)/2

print(a(nums1,nums2))