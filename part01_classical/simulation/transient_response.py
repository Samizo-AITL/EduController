# ⏱️ 1次・2次系のステップ応答を比較するスクリプト

import numpy as np
import matplotlib.pyplot as plt
import control

# --- 1次遅れ系 G1(s) = 1 / (tau s + 1) ---
tau = 1.0
G1 = control.tf([1], [tau, 1])

# --- 2次遅れ系 G2(s) = wn^2 / (s^2 + 2zeta*wn*s + wn^2) ---
wn = 2.0
zeta = 0.5
G2 = control.tf([wn**2], [1, 2*zeta*wn, wn**2])

# --- ステップ応答の描画 ---
t = np.linspace(0, 10, 500)

# 応答計算
t1, y1 = control.step_response(G1, t)
t2, y2 = control.step_response(G2, t)

# 描画
plt.figure(figsize=(10, 6))
plt.plot(t1, y1, label="1st-order (τ=1)")
plt.plot(t2, y2, label="2nd-order (ζ=0.5, ωn=2)")
plt.title("Step Response: 1st-order vs 2nd-order")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../figures/transient_response.png", dpi=300)
plt.show()
