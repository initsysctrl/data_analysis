# -*- coding: utf-8 -*-
# @Time : 2020/11/19 下午9:53
# @Author : Yepeng
# @Site :
# @Describe :广播
import numpy as np
import numpy.matlib as mt

a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([[1, 2, 3]])
print(a)
print(a.shape)
print(b)
print(b.shape)
print(a + b)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.size)
c = np.arange(1, 12, 2)
print(c)
print(c.size)
d = mt.ones((3, 3))
print(d)
print(d + 3)
e = np.arange(1, 10, 2)
print(e)
x = np.random.rand(3, 2)
print(x)
def fun1():
    pass
def fun2():
    pass
def fun3():
    fun1()
    pass
fun1()
np.array([1,2,3])