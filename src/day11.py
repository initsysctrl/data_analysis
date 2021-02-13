"""
有n个台阶，你每次只能跨一阶或两阶，上楼有几种方法？
"""
import numpy as np


def fun(n):
    if n == 1:
        print(f"1")
        return 1
    elif n == 2:
        print(f"2")
        return 2
    else:
        result = fun(n-1)+fun(n-2)
        print(result)
        return result
