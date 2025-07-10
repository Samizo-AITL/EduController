# 🛡️ hinf_synthesis_demo.py
# H∞制御の基礎的な感度関数・補償関数の確認デモ（設計自体は簡易）

import numpy as np
import matplotlib.pyplot as plt
import control

# --- プラント定義（例：2次遅れ系） ---
# G(s) = 1 / (s^2 + 0.5s + 1)
num = [1]
den = [1, 0.5, 1]
G = control.tf(num, den)

# --- 単純な比例制御器 K(s) = k ---
k = 3.0
K = control.tf([k], [1])

# --- 閉ループ系（感度関数 S, 補償関数 T） ---
L = G * K  # 開ループ
S = 1 / (1 + L)
T = L / (1 + L)

# --- 周波数特性 ---
omega = np.logspace(-2, 2, 500)
mag_S, phase_S, _ = control.bode(S, omega, Plot=False)
mag_T, phase_T, _ = control.bode(T, omega, Plot=False)

# --- ゲイン余裕/位相余裕の確認 ---
gm, pm, sm, wg, wp, ws = control.stability_margins(L, returnall=True)

# --- 描画 ---
plt.figure(figsize=(10, 6))
plt.semilogx(omega, 20*np.log10(mag_S), label='|S(jω)|')
plt.semilogx(omega, 20*np.log10(mag_T), label='|T(jω)|')
plt.axhline(0, color='k', linestyle='--')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Sensitivity and Complementary Sensitivity')
plt.grid(True, which='both')
plt.legend()
plt.tight_layout()
plt.savefig("../figures/hinf_sensitivity_response.png", dpi=300)
plt.show()
