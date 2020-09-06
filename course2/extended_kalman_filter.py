import numpy as np
import sys

delta_t = 0.5
u_k = -2
y_k = np.pi/6
S = 20
D = 40
t = 0.5

# original measurement
x_k = np.mat([0, 5]).T
P_k = np.mat([[0.01, 0], [0, 1]])

R_k = 0.01
Q_k = np.mat([[0.1, 0], [0, 0.1]])
v_k = np.random.normal(0, R_k, 1)
w_k = np.random.normal(0, 0.1, (2, 2)) #also called Q_k

F_k = np.mat([[1, delta_t], [0, 1]])
L_k = np.identity(2)
# H_k = np.mat([S/((D-x_k.item(0))**2 + S**2), 0])
H_k = np.mat([0.011, 0])
M_k = np.mat([1])

while True:
    if t == 1:
        break
    
    x_k = F_k * x_k + np.mat([0, delta_t]).T * u_k
    print('x_k\n', x_k)
    P_k = F_k * P_k * F_k.T + L_k * Q_k * L_k.T
    print('P_k\n', P_k)

    print('H_k\n', H_k)
    K_k = P_k * H_k.T * np.linalg.inv(H_k * P_k * H_k.T + (M_k * R_k * M_k.T).item(0))
    print('K_k\n', K_k)

    y_k = np.arctan(S / (D - x_k.item(0))) #+ v_k
    print('y_k:', y_k)
    x_k = x_k + K_k * (y_k.item(0) - x_k.item(0))
    print('x_k\n', x_k)

    t += delta_t

print(x_k)

# P = np.mat([[0.36, 0.5], [0.5, 1.1]])
# H = np.mat([0.011, 0])
# M = np.mat([1])
# R = np.mat([0.01])

# K = P * H.T * np.linalg.inv(H * P * H.T + M * R * M.T)
# print(K)