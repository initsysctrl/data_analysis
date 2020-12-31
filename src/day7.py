"""
斐波拉契数列 的通项式
"""
import numpy as np
# X_n=A`n-1 x_1
# 向量 x_1
x1=np.array([1,0])
# 矩阵A
A=np.array([[1,1],[1,0]])
# 求矩阵a的特征值和特征向量
ks,vs=np.linalg.eig(A)
k_1=ks[0] # 特征值1
k_2=ks[1] # 特征值2
v_1=vs[0] #特征向量1
v_2=vs[1] # 特征向量2
print(f"求矩阵A的特征值为k_1={k_1},k_2={k_2}")
print(f"求矩阵A的特征向量为v_1={v_1},v_2={v_2}")
# 求解c1 和 c2,用v1和v2 的线性组合替换x_1, c1*v_1+c2*v_2=x1
c1,c2=np.linalg.solve(vs,x1)
print(f"求解得c1={c1},c2={c2}")
# 带入元公式 xn=A`(n-1)x1=A~(n-1) (c1v_1+c2v_2)=c1A`v_1+c2Av_2=c1k_1`v_1+c2k_2`v_2
# x_n的第一个分项就是a_n
fblq=lambda n: c1*k_1**(n-1)*v_1[0]+c2*k_2**(n-1)+v_2[0]
# 测试求前50项
print([fblq(i) for i in range(1,50)])
#直接迭代求法
def fb(n:int)->int:
    if n==0 or n==1:
        return n
    else:
        return fb(n-1)+fb(n-2)

# 求1～9 项
# print([fb(i) for i in range(1,30)])