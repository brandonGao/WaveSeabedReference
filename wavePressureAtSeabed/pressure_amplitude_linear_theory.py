import numpy as np
from scipy.optimize import fsolve

# 从外部获取输入
T = float(input("input wave period T:"))
d = float(input("input water depth d:"))
H = float(input("input wave height H:"))

# 重力加速度，水容重
g = 9.81
rhow = 1000

w = 2*np.pi/T

# 用 fsolve 函数解决非线性方程
def equation(k):
    return w**2 - g*k*np.tanh(k*d)

k = fsolve(equation, 1)[0]

L = 2*np.pi/k
P0 = rhow*g*H/(2*np.cosh(k*d))

print("L:", L)
print("P0:", P0)
