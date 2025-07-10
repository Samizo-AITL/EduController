import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt

# シミュレーション：ランダムな2次元線形システム
def simulate_system(A, B, C, D, N=200):
    x = np.zeros((A.shape[0],))
    u_seq = np.random.uniform(-1, 1, (N,))
    y_seq = []
    for u in u_seq:
        x = A @ x + B * u
        y = C @ x + D * u
        y_seq.append(y)
    return u_seq, np.array(y_seq).flatten()

# データ生成
A_true = np.array([[0.9, 0.1], [0.0, 0.8]])
B_true = np.array([[0.1], [0.05]])
C_true = np.array([[1.0, 0.0]])
D_true = np.array([[0.0]])
u_seq, y_seq = simulate_system(A_true, B_true, C_true, D_true, N=300)

# ハンケル行列を作る関数
def build_hankel(data, rows):
    return np.column_stack([data[i:i+rows] for i in range(len(data) - rows)])

# パラメータ
s = 20  # ハンケル行列の行数
Up = build_hankel(u_seq[:-1], s)
Yp = build_hankel(y_seq[:-1], s)
Uf = build_hankel(u_seq[s:], s)
Yf = build_hankel(y_seq[s:], s)

# サブスペース同定（簡略化版）
W = np.vstack([Up, Yp])
U_svd, S_svd, Vh_svd = svd(W, full_matrices=False)

# 系の次数推定（ここでは2に固定）
n = 2
Ob = U_svd[:s, :n] @ np.diag(np.sqrt(S_svd[:n]))  # 観測行列の近似

print("推定された状態次元:", n)
print("観測行列 Ob（前sステップ）:
", Ob)

# 可視化：入力と出力系列
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(u_seq, label='Input u')
plt.legend(); plt.grid()
plt.subplot(2, 1, 2)
plt.plot(y_seq, label='Output y')
plt.legend(); plt.grid()
plt.suptitle("System Input and Output")
plt.tight_layout()
plt.show()
