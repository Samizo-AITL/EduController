# lqr_design.py
# 倒立振子（カート付き）の状態空間モデルに対する LQR 制御器設計

import numpy as np
import matplotlib.pyplot as plt
from control import ss, lqr, initial_response

# パラメータ設定
M = 1.0     # カート質量 [kg]
m = 0.1     # 振子質量 [kg]
l = 0.5     # 振子長さ [m]
g = 9.81    # 重力加速度 [m/s^2]

# 状態空間モデル A, B
A = np.array([
    [0, 1, 0, 0],
    [0, 0, -m*g/M, 0],
    [0, 0, 0, 1],
    [0, 0, (M + m)*g/(M*l), 0]
])

B = np.array([
    [0],
    [1/M],
    [0],
    [-1/(M*l)]
])

# 出力行列（観測はカート位置と角度）
C = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0]
])
D = np.zeros((2, 1))

# 状態空間システム
sys = ss(A, B, C, D)

# LQR設計
Q = np.diag([10, 1, 10, 1])  # 状態重み
R = np.array([[0.01]])       # 入力重み
K, S, E = lqr(sys, Q, R)     # ゲインK, リカッチ方程式S, 固有値E

# 初期状態
x0 = np.array([0.1, 0, 0.2, 0])  # 少し位置と角度をずらす

# 閉ループ系のA行列（A - BK）
A_cl = A - B @ K
sys_cl = ss(A_cl, B, C, D)

# 応答計算
time = np.linspace(0, 5, 500)
t_out, y_out = initial_response(sys_cl, T=time, X0=x0)

# プロット
plt.figure(figsize=(8,4))
plt.plot(t_out, y_out[0], label="Cart Position x(t)")
plt.plot(t_out, y_out[1], label="Pendulum Angle θ(t)")
plt.title("LQR Controlled Response (Initial Condition)")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ゲイン行列出力
print("LQR Gain K =", K)
