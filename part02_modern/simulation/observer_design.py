# 👁️ observer_design.py
# 状態推定器（オブザーバ）設計とシミュレーション

import numpy as np
import matplotlib.pyplot as plt
import control

# --- 状態空間モデル定義 ---
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# --- 状態フィードバックゲイン（任意のK） ---
K = control.place(A, B, [-2, -4])
print("フィードバックゲイン K:", K)

# --- オブザーバゲイン設計（極配置） ---
desired_observer_poles = [-5, -6]
L = control.place(A.T, C.T, desired_observer_poles).T
print("オブザーバゲイン L:")
print(L)

# --- 拡張系（オブザーバ付きシステム）の構成 ---
A_obs = np.block([
    [A - B @ K, B @ K],
    [np.zeros_like(A), A - L @ C]
])
B_obs = np.vstack([B, np.zeros_like(B)])
C_obs = np.hstack([C, np.zeros_like(C)])
D_obs = np.array([[0]])

# --- 応答計算（ステップ入力） ---
sys_obs = control.ss(A_obs, B_obs, C_obs, D_obs)
T = np.linspace(0, 10, 500)
T, yout = control.step_response(sys_obs, T)

# --- 描画 ---
plt.figure()
plt.plot(T, yout, label="y(t): 推定ベース制御出力")
plt.title("Step Response with State Observer")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../figures/observer_response.png", dpi=300)
plt.show()
