import numpy as np
import matplotlib.pyplot as plt
import control

# --- 対象システムの定義（例：二次遅れ系） ---
# G(s) = 1 / (s^2 + 2s + 1)
G = control.tf([1], [1, 2, 1])

# --- ゲイン余裕・位相余裕の計算 ---
gm, pm, wg, wp = control.margin(G)

print("=== 安定余裕の計算結果 ===")
print(f"Gain Margin (GM): {20*np.log10(gm):.2f} dB at ω = {wp:.2f} rad/s")
print(f"Phase Margin (PM): {pm:.2f}° at ω = {wg:.2f} rad/s")

# --- ボード線図の描画 ---
plt.figure(figsize=(10, 6))

mag, phase, omega = control.bode(G, dB=True, deg=True, Plot=False)

# ゲインプロット
plt.subplot(2, 1, 1)
plt.semilogx(omega, 20*np.log10(mag), label='Gain')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(wg, color='r', linestyle=':', label='PM freq')
plt.ylabel("Gain [dB]")
plt.grid(True)
plt.legend()

# 位相プロット
plt.subplot(2, 1, 2)
plt.semilogx(omega, phase * 180/np.pi, label='Phase')
plt.axhline(-180, color='gray', linestyle='--')
plt.axvline(wp, color='r', linestyle=':', label='GM freq')
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Phase [deg]")
plt.grid(True)
plt.legend()

plt.suptitle("Bode Plot with Gain/Phase Margins")
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig("../figures/phase_gain_margin_example.png", dpi=300)
plt.show()
