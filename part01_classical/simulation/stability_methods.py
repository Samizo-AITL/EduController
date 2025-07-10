# 🧮 安定性判別法：Routh表・根軌跡・ナイキスト線図の確認用スクリプト

import numpy as np
import matplotlib.pyplot as plt
import control

# --- 対象システム（例：3次系） ---
# G(s) = K / (s^3 + 4s^2 + 5s + K)
K = 5
num = [K]
den = [1, 4, 5, K]
G = control.tf(num, den)

print("=== 対象システム ===")
print(G)

# --- 根軌跡の描画 ---
plt.figure()
control.root_locus(G, Plot=True)
plt.title("Root Locus")
plt.grid(True)
plt.tight_layout()
plt.savefig("../figures/root_locus_example.png", dpi=300)

# --- ナイキスト線図 ---
plt.figure()
control.nyquist_plot(G)
plt.title("Nyquist Plot")
plt.tight_layout()
plt.savefig("../figures/nyquist_example.png", dpi=300)

# --- Routh-Hurwitz表の計算（簡易版） ---
def routh_table(coeffs):
    n = len(coeffs)
    m = (n + 1) // 2
    routh = np.zeros((n, m))
    routh[0, :len(coeffs[::2])] = coeffs[::2]
    routh[1, :len(coeffs[1::2])] = coeffs[1::2]

    for i in range(2, n):
        for j in range(m - 1):
            a = routh[i-2, 0]
            b = routh[i-1, 0]
            c = routh[i-2, j+1]
            d = routh[i-1, j+1]
            routh[i, j] = ((b * c) - (a * d)) / (b if b != 0 else 1e-6)
    return routh

print("\n=== Routh-Hurwitz 表 ===")
R = routh_table(den)
print(np.round(R, 3))
