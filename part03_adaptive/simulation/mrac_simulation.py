# 🔄 mrac_simulation.py
# MITルールに基づく MRAC (Model Reference Adaptive Control) の簡易シミュレーション

import numpy as np
import matplotlib.pyplot as plt

# --- シミュレーションパラメータ ---
dt = 0.01
T = 20
time = np.arange(0, T, dt)

# --- 参照モデル（1次系） ---
T_m = 1.0
a_m = 1.0 / T_m
y_m = 0.0  # 参照モデル出力

# --- 実プラント（未知パラメータ） ---
k_p = 2.0
tau_p = 1.5
a_p = 1.0 / tau_p
b_p = k_p / tau_p
y = 0.0  # プラント出力

# --- 可変制御器の初期値（θ1: rゲイン, θ2: yゲイン） ---
theta1 = 0.5
theta2 = 0.0

# --- 適応律パラメータ（学習率） ---
gamma1 = 2.0
gamma2 = 2.0

# --- ログ格納用 ---
y_log, ym_log, u_log, e_log = [], [], [], []

# --- メインループ ---
for t in time:
    # 目標入力（ステップ入力）
    r = 1.0 if t > 1.0 else 0.0

    # 参照モデル
    dy_m = -a_m * y_m + a_m * r
    y_m += dy_m * dt

    # 制御入力
    u = theta1 * r + theta2 * y

    # プラント
    dy = -a_p * y + b_p * u
    y += dy * dt

    # 適応誤差
    e = y - y_m

    # MITルールによる更新
    dtheta1 = -gamma1 * e * r
    dtheta2 = -gamma2 * e * y
    theta1 += dtheta1 * dt
    theta2 += dtheta2 * dt

    # ログ記録
    y_log.append(y)
    ym_log.append(y_m)
    u_log.append(u)
    e_log.append(e)

# --- 描画 ---
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, y_log, label='Plant Output y(t)')
plt.plot(time, ym_log, '--', label='Reference Model y_m(t)')
plt.ylabel('Output')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, u_log, label='Control Input u(t)')
plt.plot(time, e_log, label='Tracking Error e(t)')
plt.xlabel('Time [s]')
plt.ylabel('Control / Error')
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig("../figures/mrac_response.png", dpi=300)
plt.show()
