# 单摆系统的微分方程
import numpy as np
import matplotlib.pyplot as plt

# 重力加速度
g = 0.98
# 单摆长度
L = 2
# 空气阻力系数
mu = 0.1
# 初始角度
THEAT_0 = np.pi/3
# 初始角速度
THEAT_DOT_0 = 0


def get_theta_double_dot(theat, theat_dot):
    """[求角速度的加速度]

    Args:
        theat ([type]): [角度]
        theat_dot ([type]): [角速度]

    Returns:
        [type]: [加速度]
    """
    return -mu*theat_dot-(g/L)*np.sin(theat)


def theat(t):
    """[求角度]

    Args:
        t ([type]): [时间t]

    Returns:
        [type]: [时间序列、理想模型下角度序列，实际角度序列、实际角速度序列、实际加速度序列]
    """
    theat = THEAT_0  # 角度 初始化
    theat_dot = THEAT_DOT_0  # 角速度 初始化
    delta_t = 0.01  # 微分时间
    x_data = []  # 时间序列
    y_data_0 = []
    y_data_1 = []
    y_data_2 = []
    y_data_3 = []

    for i in np.arange(0, t, delta_t):
        theat_double_dot = get_theta_double_dot(theat, theat_dot)
        theat += theat_dot*delta_t
        theat_dot += theat_double_dot*delta_t
        print(i, theat)
        x_data.append(i)
        y_data_0.append(THEAT_0*np.cos(np.sqrt(g/L)*i))
        y_data_1.append(theat)
        y_data_2.append(theat_dot)
        y_data_3.append(theat_double_dot)
    return x_data, y_data_0, y_data_1, y_data_2, y_data_3


# 测试。。。。。。。。。。。。
t = 100  # 时间
x, y0, y1, y2, y3 = theat(t)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

plt.subplot(2, 2, 1)
plt.xlabel('时间')
plt.title('理想角度')
plt.plot(x, y0, color='red', label='theta-temp')


plt.subplot(2, 2, 2)
plt.xlabel('时间')
plt.title('实际角度 theta')
plt.plot(x, y1, color='red')

plt.subplot(2, 2, 3)
plt.xlabel('时间')
plt.title('实际角速度 theta_dot')
plt.plot(x, y2, color='green')

plt.subplot(2, 2, 4)
plt.xlabel('时间')
plt.title('实际加速度 theta_double_dot')

plt.plot(x, y3, color='blue')
plt.tight_layout()
plt.show()
