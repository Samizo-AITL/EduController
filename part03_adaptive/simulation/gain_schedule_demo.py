# 🔀 gain_schedule_demo.py
# ゲインスケジューリングによる簡単な線形補間制御のシミュレーション

import numpy as np
import matplotlib.pyplot as plt

# --- シミュレーション設定 ---
dt = 0.01
T = 10
time = np.arange(0, T, dt)

# --- 動作点ごとのゲイン定義（例：PIDゲイン） ---
K1 = 1.0  # ρ = 0.0 のときのゲイン（例：通常時）
K2 = 3.0  # ρ = 1.0 のときのゲイン（例：高速応答）

# --- スケジューリング関数（線形補間） ---
def gain_schedule(rho):
    return (1 - rho) * K1 + rho * K2

# --- プラント（1次遅れ系） ---
tau = 1.0
y = 0.0

# --- ログ変数 ---
y_log, u_log, rho_log = [], [], []

# --- メインループ ---
for t in time:
    # 目標値（ステップ入力）
    r = 1.0

    # スケジューリング変数（時間に応じて変化：0→1）
    rho = min(t / T, 1.0)

    # 時変ゲインの計算
    K = gain_schedule(rho)

    # 制御入力（比例制御）
    u = K * (r - y)

    # プラント応答
    dy = (-y + u) / tau
    y += dy * dt

    # ログ
    y_log.append(y)
    u_log.append(u)
    rho_log.append(rho)

# --- 結果描画 ---
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, y_log, label='Output y(t)')
plt.plot(time, [1.0]*len(time), '--', label='Reference r(t)')
plt.ylabel('Output')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, u_log, label='Control Input u(t)')
plt.plot(time, rho_log, label='Scheduling Var ρ(t)', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('u(t), ρ(t)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig("../figures/gain_schedule_response.png", dpi=300)
plt.show()
