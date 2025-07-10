# 📉 任意の伝達関数に対するボード線図を描画するスクリプト

import numpy as np
import matplotlib.pyplot as plt
import control

# --- 対象システム（例：1次遅れ系） ---
# G(s) = 1 / (s + 1)
G = control.tf([1], [1, 1])

# --- ボード線図の描画 ---
plt.figure(figsize=(10, 6))

mag, phase, omega = control.bode(G, dB=True, deg=True, Plot=False)

# ゲインプロット
plt.subplot(2, 1, 1)
plt.semilogx(omega, 20 * np.log10(mag), label='Gain')
plt.axhline(0, color='gray', linestyle='--')
plt.ylabel("Gain [dB]")
plt.grid(True)
plt.legend()

# 位相プロット
plt.subplot(2, 1, 2)
plt.semilogx(omega, phase * 180 / np.pi, label='Phase')
plt.axhline(-180, color='gray', linestyle='--')
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Phase [deg]")
plt.grid(True)
plt.legend()

plt.suptitle("Bode Plot of G(s) = 1 / (s + 1)")
plt.tight_layout()
plt.savefig("../figures/bode_example.png", dpi=300)
plt.show()
