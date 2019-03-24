# -*- coding: utf-8 -*-

from typing import List
'''
------------------------------------------------------------
File Name: buying_and_selling_stocks.py
Description : 
Project: Python_Algorithm_Example
Last Modified: Monday, 25th March 2019 1:29:57 am
-------------------------------------------------------------
'''

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
"""

"""
Given an array, its ith element is the price of the first day of a given stock.
If you only allow a maximum of one transaction (ie buy and sell a stock), design an algorithm to calculate the maximum profit you can get.
Note that you cannot sell stocks before buying stocks.
"""

# 1 recursion


def recursionMaxProfix(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    return max(prices[- 1] - min(prices[:- 1]),
               recursionMaxProfix(prices[:- 1]))


print(recursionMaxProfix([7,1,5,3,6,4]))

# 2 iteration

def maxProfit(prices: List[int]):
    result = [0]
    if len(prices) < 2:
        return 0
    minPrice = prices[0]
    for i in range(1, len(prices)):
        minPrice = min(minPrice, prices[i - 1])
        result.append(max(prices[i] - minPrice, result[i - 1]))
    return result[-1]

print(maxProfit([7,1,5,3,6,4]))
