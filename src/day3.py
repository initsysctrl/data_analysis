# -*- coding: utf-8 -*-
# @Time : 2020/11/20 下午10:01
# @Author : Yepeng
# @Site :
# @Describe :
import numpy as np

arr = np.arange(0, 15).reshape(5, 3)
print(arr)

print(arr[arr[:, 0] > 1])
