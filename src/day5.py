import numpy as np
# 行向量
v = np.array([[0, 1, 2]])
print(f"行向量v1=\n{v}",v.shape)
# 列向量
v = np.array([[0], [1], [2]])
print(f"列向量v2=\n{v}",v.shape)

v=np.array([1,2,3])
print(f"真实向量v={v}",v.shape)
print(f"真实向量v={v.T}",v.shape)

# 创建矩阵
matrix = np.mat([[1, 2], [3, 4]])

print(f"矩阵matrix=\n{matrix}")
print(f"矩阵matrix的转置=\n{matrix.T}")

f = np.vectorize(lambda i: i*i)

print(f"矩阵函数:\n{f(matrix)}")
# 矩阵的秩

print(f"矩阵的秩\n{np.linalg.matrix_rank(matrix)}")

# 行列式
print(f"矩阵的行列式\n{np.linalg.det(matrix)}")

# 迹
print(f"矩阵的迹\n{matrix.trace()}")

# 特征向量和特征值
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"特征值和特征向量\n {eigenvalues}\n{eigenvectors}")

# 矩阵的逆
m = np.mat([[1, 2], [3, 4]])
result = np.linalg.inv(m)
print(f"矩阵的逆矩阵\n {result}")

# 矩阵的左乘
m1 = np.mat([[1, 2], [3, 4]])
m2 = np.mat([[0, 1], [1, 2]])
print(f"np.dot(m1, m2)=\n{np.dot(m1, m2)}")
print(f"矩阵的左乘\n {m1 @ m2}\n{m2 @ m1}")
print(f"矩阵的点乘\n {m1 * m2}\n {m2*m1}")


# 向量的点积
v1 = np.array([1, 0])
v2 = np.array([0, 1])
d1 = np.dot(v1, v2)
d2 = np.vdot(v1, v2)
d3 = np.inner(v1, v2)
d4 = np.outer(v1, v2)
d5 = np.cross(v1, v2)
print(f"d1= {d1}")
print(f"d2= {d2}")
print(f"d3={d3}")
print(f"d4=\n{d4}")
print(f"d5\5=\n{d5}")
print("---------------------")
# TT^-1
m = np.mat([[1, 2], [2, 3]])
m_inv = np.linalg.inv(m)
print(m @ m_inv)
print(m_inv)

# 矩阵x向量
print("----------")
m = np.array([[1, 2, 3], [3, 4, 5]])
print(m, m.shape, type(m))
# v = np.array([[1], [2], [3]])
v = np.array([1, 2, 3]).T
print(v, v.shape, type(v))
result = np.dot(m, v)
print(result, result.shape, type(result))

# 矩阵x矩阵
m1 = np.mat([[1, 2], [3, 4]])
m2 = np.mat([[2, 2], [1, 1]])
result = np.dot(m1, m2)
# result = m1 @ m2 等价
# result = m1 * m2 等价
print(result)
# 矩阵乘向量
v=np.array([1,2,3]).T
print(v,v.shape)
m=np.mat([[1,2,3],[1,0,1]])

result=np.dot(m,v)
print(f"矩阵x 向量={result} {type(result)} {result.shape}")
print("-------------")
# 向量的内积
v1 = np.array([0,2,1])
v2 = np.array([2,0,1])
inner_product = v1 @ v2
inner_product = np.inner(v1, v2)
print(inner_product)

# 向量的外积/叉积
cross_product=np.cross(v1,v2)
print(cross_product)

# 方程求解
m=np.array([[1,0],[0,1]])
y=np.array([[2,0],[0,2]])
result=np.linalg.solve(m,y)
print(result)