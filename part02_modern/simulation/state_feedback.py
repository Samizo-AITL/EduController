# 🎛️ state_feedback.py
# 状態フィードバック制御（極配置）による制御応答確認

import numpy as np
import matplotlib.pyplot as plt
import control

# --- システム定義 ---
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# --- 極配置によるゲイン計算 ---
desired_poles = [-2, -5]
K = control.place(A, B, desired_poles)
print("状態フィードバックゲイン K:")
print(K)

# --- 閉ループ系構築 ---
A_cl = A - B @ K
sys_cl = control.ss(A_cl, B, C, D)

# --- ステップ応答 ---
T = np.linspace(0, 10, 500)
T, yout = control.step_response(sys_cl, T)

# --- 図出力 ---
plt.figure()
plt.plot(T, yout, label="y(t): 状態フィードバック応答")
plt.title("Step Response with State Feedback")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../figures/state_feedback_response.png", dpi=300)
plt.show()
