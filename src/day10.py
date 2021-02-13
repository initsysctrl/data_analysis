import numpy as np
import pandas as pd

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 零数组
array = np.zeros((3, 3))
# 填充制定元素的数组
array = np.full((2, 2), 9)
# 单位矩阵，对角线为1，其余为0
array = np.eye(5, 5)
# 随机
array = np.random.rand(2, 2, 2)
# 步进方式创建，同时重构shape
array = np.arange(start=1, stop=10, step=1).reshape(3, 3)

print(array)
# 数组的元素个数
print(array.size)
# 数组的形状 shape
print(array.shape)
# # 秩，即轴的数量或维度的数量
print(array.ndim)
array = np.arange(start=1, stop=100, step=1).reshape(33, 3)
df = pd.DataFrame(array, columns=list('abc'))
print(df)
x = ''.join(['a', 'b', 'c'])
print(x)
print(type(x))
