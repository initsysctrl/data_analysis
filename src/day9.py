# 常微分方程的数值解法
import numpy as np
# import matplotlib.pyplot as plt

# 重力加速度
g = 0.98
# 单摆长度
L = 2
# 空气阻力系数
mu = 0.5
# 初始角度
THEAT_0 = np.pi/3
# 初始角速度
THEAT_DOT_0 = 0


def get_theta_double_dot(theat, theat_dot):
    """[summary]

    Args:
        theat ([type]): [description]
        theat_dot ([type]): [description]

    Returns:
        [type]: [description]
    """
    return -1*mu*theat_dot-(g/L)*np.sin(theat)


def theat(t):
    """[summary]

    Args:
        t ([type]): [description]

    Returns:
        [type]: [description]
    """
    theat = THEAT_0
    theat_dot = THEAT_DOT_0
    delta_t = 0.01
    for i in np.arange(0, t, delta_t):
        theat_double_dot = get_theta_double_dot(theat, theat_dot)
        theat += theat_dot*delta_t
        theat_dot += theat_double_dot*delta_t
        pass
    return theat


t =10
t_array=np.arange(0,t,0.1)
print(t_array)
print(f"t={t},theat({t})={theat(t)}")
# plt.plot()