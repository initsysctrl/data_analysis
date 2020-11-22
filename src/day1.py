# -*- coding: utf-8 -*-
# @Time : 2020/11/17 下午10:19
# @Author : Yepeng
# @Site : 
# @Describe :
import numpy as np
import pandas as pd
import numpy.matlib as mt
# 直接数组创建矩阵

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 随机数创建矩阵
arr = np.random.rand(4, 3)
arr = np.random.random(10)

arr = np.random.randint(0, 10, 12).reshape(3, 4)
arr = np.array(np.arange(0, 12)).reshape(3, 4)
# 全是0的矩阵
# arr = np.zeros(shape=(3, 4))
# 全是1的矩阵
# arr = np.ones(3)
# 对角矩阵 5*5
# arr = np.eye(5)
# 这是一个2*4的narray
print(arr)
print(arr.size)
print(arr.shape)

# 索引
# print(arr[1, 3])
# 切片
print(arr[:, 1])  # 第二列
print(arr[1, :])  # 第二
# 重新赋值
# new_arr = np.array([[999, 999], [888, 888]])
# arr[0:2, 0:2] = new_arr
# print(arr)
# 筛选-面具理论
mask = (arr[:, 1] > 4) & (arr[:, 2] > 7)
print(arr[mask])
arrr = np.array([1, 2, 3])
print(arrr.shape)
print(np.zeros((3, 2)))
print(mt.zeros((3, 2)))
# print(mt.ones((2, 2)))
